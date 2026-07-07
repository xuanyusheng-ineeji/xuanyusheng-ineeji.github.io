Add a GitHub project to the portfolio website.

Usage: /add-project <github-url> [industry|personal]

Arguments: $ARGUMENTS

---

## Phase 1 — Collect Information

### 1.1 Parse arguments
Extract the GitHub URL and category (`industry` or `personal`, default: `industry`).
Derive owner/repo. Raw base: `https://raw.githubusercontent.com/{owner}/{repo}/HEAD`

### 1.2 Try documentation files first
Attempt to fetch (use WebFetch on each):
- `{raw_base}/PROJECT_SUMMARY.md`
- `{raw_base}/README.md`
- `{raw_base}/CLAUDE.md`

**If at least one file returns content → go to Phase 2.**

### 1.3 Fallback: read the source code
If no documentation files exist, explore the repo structure via the GitHub API or by fetching:
- `https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1`

From the file tree, identify and read the most informative files:
- Entry points: `main.py`, `app.py`, `index.ts`, `server.js`, `Makefile`, etc.
- Config: `pyproject.toml`, `package.json`, `requirements.txt`, `docker-compose.yml`
- Core logic: up to 5 key source files based on the file tree structure

Infer the project's purpose, architecture, and tech stack from the code itself.

---

## Phase 2 — Draft the Entry

From all collected content, draft these fields:
- **title**: Project name + one-line tagline
- **org**: Organization and team (omit if personal project)
- **badge**: Short label (e.g. `"ineeji · 2025"`)
- **description**: 2–3 sentences on what the project does and its impact
- **bullets**: 3–5 key points in `**Aspect**: detail` format covering input, core logic, output, notable technical decisions
- **tech**: Key technologies joined by ` · `

---

## Phase 3 — Verify (do not skip)

Re-read the source material with fresh eyes and check every drafted claim:

| Claim in draft | Evidence found in repo? |
|----------------|------------------------|
| Each bullet point | Verify against actual file content |
| Tech stack items | Confirm each appears in code / config |
| Description sentences | Must not overstate or invent features |

**For each claim that cannot be verified, either remove it or soften the language.**
Show the verification table in your response so the user can see what was confirmed vs. adjusted.

---

## Phase 4 — Handle image

Check `images/` for an existing relevant image. If none:
- Generate an architecture diagram with matplotlib (same style as `images/data_collector_arch.png`)
- Save to `images/{repo_name}_arch.png`

Set `image: "/images/{filename}"`.

---

## Phase 5 — Write to registry

Append to `_data/projects.yml` under the correct category using this schema:

```yaml
- title: "..."
  org: "..."           # omit entirely for personal projects
  github: "https://github.com/..."
  image: "/images/..."
  badge: "... · YYYY"
  description: >
    ...
  bullets:
    - "**Aspect**: detail"
    - "**Aspect**: detail"
    - "**Aspect**: detail"
  tech: "Tech1 · Tech2 · Tech3"
```

Do NOT modify `_pages/projects.md` — it auto-renders from the data file.

---

## Phase 6 — Report

Show:
1. How information was collected (docs / source code fallback)
2. The verification table from Phase 3
3. The final YAML entry that was written
