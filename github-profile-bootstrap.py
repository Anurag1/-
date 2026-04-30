#!/usr/bin/env python3
"""Bootstrap production-grade defaults across all repositories for a GitHub user/org.

Usage:
  GITHUB_TOKEN=... python github-profile-bootstrap.py --owner Anurag1
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API = "https://api.github.com"


def request_json(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> tuple[int, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url=url, method=method, data=body)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8")
        try:
            parsed = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            parsed = {"message": raw}
        return exc.code, parsed


def iter_repos(owner: str, token: str, include_archived: bool) -> list[dict[str, Any]]:
    repos: list[dict[str, Any]] = []
    page = 1
    while True:
        q = urllib.parse.urlencode({"per_page": 100, "page": page, "sort": "updated"})
        status, data = request_json("GET", f"{API}/users/{owner}/repos?{q}", token)
        if status != 200:
            raise RuntimeError(f"Failed to list repos: HTTP {status}: {data}")
        if not data:
            break
        for repo in data:
            if repo.get("fork"):
                continue
            if repo.get("archived") and not include_archived:
                continue
            repos.append(repo)
        page += 1
    return repos


def configure_repo(owner: str, repo_name: str, token: str, default_branch: str, dry_run: bool) -> None:
    repo_url = f"{API}/repos/{owner}/{repo_name}"
    patch_payload = {
        "has_issues": True,
        "has_projects": True,
        "has_wiki": False,
        "allow_squash_merge": True,
        "allow_rebase_merge": True,
        "allow_merge_commit": False,
        "delete_branch_on_merge": True,
    }

    protection_payload = {
        "required_status_checks": {"strict": True, "contexts": []},
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 1,
        },
        "restrictions": None,
        "required_linear_history": True,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "block_creations": False,
        "required_conversation_resolution": True,
        "lock_branch": False,
        "allow_fork_syncing": True,
    }

    dependabot_payload = {"state": "enabled"}

    if dry_run:
        print(f"[dry-run] Would PATCH {repo_url}")
        print(f"[dry-run] Would PUT {repo_url}/branches/{default_branch}/protection")
        print(f"[dry-run] Would PUT {repo_url}/vulnerability-alerts")
        print(f"[dry-run] Would PUT {repo_url}/automated-security-fixes")
        print(f"[dry-run] Would PUT {repo_url}/private-vulnerability-reporting")
        return

    status, data = request_json("PATCH", repo_url, token, patch_payload)
    if status not in (200, 201):
        print(f"  ! repo settings failed: HTTP {status} {data}")

    status, data = request_json(
        "PUT", f"{repo_url}/branches/{default_branch}/protection", token, protection_payload
    )
    if status not in (200, 201):
        print(f"  ! branch protection failed: HTTP {status} {data}")

    for endpoint in [
        "vulnerability-alerts",
        "automated-security-fixes",
        "private-vulnerability-reporting",
    ]:
        status, data = request_json("PUT", f"{repo_url}/{endpoint}", token, dependabot_payload)
        if status not in (200, 201, 204):
            print(f"  ! {endpoint} failed: HTTP {status} {data}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", required=True, help="GitHub username or org name")
    parser.add_argument("--default-branch", default="main", help="Branch to protect (default: main)")
    parser.add_argument("--include-archived", action="store_true", help="Include archived repositories")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without mutating repositories")
    parser.add_argument("--sleep", type=float, default=0.2, help="Seconds to sleep between repos")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Missing GITHUB_TOKEN environment variable.", file=sys.stderr)
        return 2

    repos = iter_repos(args.owner, token, args.include_archived)
    print(f"Found {len(repos)} repositories to configure for {args.owner}.")

    for idx, repo in enumerate(repos, start=1):
        name = repo["name"]
        print(f"[{idx}/{len(repos)}] Configuring {name}")
        configure_repo(args.owner, name, token, args.default_branch, args.dry_run)
        time.sleep(args.sleep)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
