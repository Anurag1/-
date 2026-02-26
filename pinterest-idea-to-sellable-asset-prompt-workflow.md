# Pinterest Idea → Sellable Asset: Exact Prompt Workflow

Use this sequence to turn a single Pinterest idea into a real product/content asset with OpenAI.

## How to run
- Copy each prompt block into ChatGPT/OpenAI.
- Replace placeholders in `[brackets]`.
- Do not skip outputs; each step feeds the next.

---

## Step 1) Trend extraction from Pinterest inputs

**Input you provide**
- Topic: `[e.g., small bedroom organization]`
- Audience: `[e.g., renters in their 20s]`
- 10–20 observed pins (title + short description + visual notes)

**Prompt**
```text
You are a product strategist and content analyst.

I will give you Pinterest observations. Your job is to extract commercial opportunities.

Context:
- Topic: [TOPIC]
- Audience: [AUDIENCE]
- Goal: identify what people actually want, then propose assets they would buy or save.

Pinterest observations:
[PASTE PIN TITLES, DESCRIPTIONS, VISUAL PATTERNS]

Return:
1) Top 10 repeated themes (with estimated intent: inspiration, how-to, checklist, template, shopping).
2) Top 10 pain points/frictions hidden in the pins.
3) 10 product/content opportunities ranked by:
   - demand signal strength (1-5)
   - ease to produce (1-5)
   - monetization potential (1-5)
4) Pick the single best opportunity and explain why in 5 bullets.
```

**Output needed before Step 2**
- One chosen opportunity + target audience + core promise.

---

## Step 2) Offer definition (what exactly gets sold)

**Prompt**
```text
Act as a direct-response product marketer.

Chosen opportunity:
[PASTE WINNING OPPORTUNITY]

Create a clear offer definition.

Return:
1) Product type (template pack, mini-guide, Notion system, checklist bundle, etc.).
2) Exact transformation statement:
   "From [current state] to [desired state] in [timeframe] without [common frustration]."
3) Buyer persona snapshot (pain, desire, objections, buying trigger).
4) Product deliverables list (specific files/pages/modules).
5) Version ladder:
   - Free lead magnet
   - Core paid offer
   - Premium upsell
6) Price test range with rationale.
```

**Output needed before Step 3**
- Finalized product structure + pricing hypothesis.

---

## Step 3) Build the product contents

**Prompt**
```text
You are now the product builder.

Build the full first version of this offer:
[PASTE OFFER DEFINITION]

Constraints:
- Practical, beginner-friendly, no fluff.
- Must be usable immediately after download.

Return:
1) Complete product outline.
2) Full draft content for each section/module.
3) Reusable templates/checklists/scripts included in the product.
4) "Quick-start" one-page version.
5) Branded naming options (10 names).
```

**Output needed before Step 4**
- Draft deliverables that can be exported as PDF/Notion/Canva assets.

---

## Step 4) Listing copy (Etsy/Gumroad/Shopify)

**Prompt**
```text
Act as an ecommerce conversion copywriter.

Using this product draft:
[PASTE STEP 3 OUTPUT]

Write:
1) 15 product title options (SEO-aware, clear, not spammy).
2) Product subtitle/tagline options (10).
3) Full sales description with structure:
   - Hook
   - Problem
   - Promise
   - What’s included
   - Who it’s for
   - How it works
   - FAQ (8 objections)
   - CTA
4) Bullet benefits (20) and feature-to-benefit mapping.
5) Keywords/tags (30) grouped by intent.
```

**Output needed before Step 5**
- Final listing page copy + keywords.

---

## Step 5) Pinterest distribution assets

**Prompt**
```text
Act as a Pinterest growth strategist + creative director.

Product and listing details:
[PASTE STEP 4 OUTPUT]

Generate:
1) 30 Pinterest pin headline variants.
2) 30 pin descriptions (SEO-friendly, natural language).
3) 10 visual concept briefs for pins (layout, text hierarchy, style, CTA).
4) 3 weekly posting schedules (light/medium/aggressive).
5) Board strategy:
   - board names
   - board descriptions
   - first 20 pin topics
6) UTM naming convention to track performance by pin concept.
```

**Output needed before Step 6**
- Ready-to-design pin copy + publishing calendar.

---

## Step 6) Launch content (email + short-form)

**Prompt**
```text
Act as a launch copywriter.

Using this offer:
[PASTE KEY DETAILS]

Create:
1) 5-email launch sequence:
   - Teaser
   - Problem agitation
   - Value/demo
   - Social proof angle
   - Last chance
2) 14 short-form posts (IG/Threads/X) with hooks + CTA.
3) 3 blog/newsletter drafts that pre-sell the offer.
4) A/B test matrix for hooks, CTA styles, and price framing.
```

---

## Step 7) Validation + iteration loop

**Prompt**
```text
Act as a growth analyst.

Here are week-1 metrics:
- Impressions: [X]
- Outbound clicks: [X]
- CTR: [X]
- Product page views: [X]
- Conversion rate: [X]
- Revenue: [X]
- Top pins: [LIST]
- Lowest performers: [LIST]

Return:
1) Diagnosis of bottlenecks by funnel stage.
2) 5 highest-impact changes for next 7 days.
3) 3 new product variations to test.
4) Revised pin/content plan for week 2.
```

---

## One-shot master prompt (optional)

```text
You are my end-to-end Pinterest-to-product operator.
Goal: Turn one Pinterest trend into a sellable digital asset in 48 hours.

Inputs:
- Topic: [TOPIC]
- Audience: [AUDIENCE]
- Pinterest observations: [PASTE]
- Preferred format: [PDF / Notion / Canva / etc.]
- Monetization channel: [Etsy / Gumroad / Shopify]

Execute these stages in order and label each section clearly:
1) Trend extraction
2) Opportunity scoring + winner selection
3) Offer definition
4) Product draft build
5) Listing copy + SEO tags
6) Pinterest pin copy + board strategy + calendar
7) Email/social launch assets
8) Week-1 KPI targets and iteration plan

For each stage include:
- Output
- Why this is the best choice
- "Ready to publish" assets
- Any assumptions that need my confirmation
```

## Minimal operating cadence
- **Day 1:** Steps 1–3 (define + build asset)
- **Day 2:** Steps 4–6 (listing + traffic + launch)
- **Day 7 review:** Step 7 (iterate from metrics)

