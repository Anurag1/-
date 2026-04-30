# GitHub Profile Repository Standardization (Anurag1)

This repo includes `github-profile-bootstrap.py`, a one-command script to apply baseline production settings across repositories.

## What it configures

- Repository defaults (`issues`, `projects`, merge settings, delete branch on merge).
- Branch protection for a chosen default branch (default `main`).
- Security baseline endpoints:
  - vulnerability alerts
  - automated security fixes
  - private vulnerability reporting

## Usage

```bash
export GITHUB_TOKEN="<token-with-repo-and-admin-rights>"
python github-profile-bootstrap.py --owner Anurag1 --dry-run
python github-profile-bootstrap.py --owner Anurag1
```

## Notes

- Use `--default-branch master` if older repos do not use `main`.
- The script skips forks by default.
- Add `--include-archived` to include archived repositories.
- Run `--dry-run` first in production environments.
