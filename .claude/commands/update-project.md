Update an existing project entry in the portfolio.

Usage: /update-project <github-url-or-project-title>

Arguments: $ARGUMENTS

---

## Phase 1 — Locate existing entry

Read `_data/projects.yml` and find the entry matching the GitHub URL or title (partial match OK).

---

## Phase 2 — Collect latest information

Use the entry's `github` field. Raw base: `https://raw.githubusercontent.com/{owner}/{repo}/HEAD`

### 2.1 Try documentation files
Fetch: `PROJECT_SUMMARY.md`, `README.md`, `CLAUDE.md`

### 2.2 Fallback: read source code
If no docs exist, fetch the file tree via:
`https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1`

Read entry points, config files, and up to 5 key source files to understand the current state of the project.

---

## Phase 3 — Verify current entry against repo

Compare each field of the existing YAML entry against the fetched content:

| Field | Current value | Verified? | Needs update? |
|-------|--------------|-----------|---------------|
| description | ... | ✓/✗ | yes/no |
| each bullet | ... | ✓/✗ | yes/no |
| tech stack | ... | ✓/✗ | yes/no |

**Flag any claim in the current entry that is no longer accurate or is overstated.**

---

## Phase 4 — Apply updates

Edit only the fields that changed. Preserve all other entries in `_data/projects.yml` exactly.

If the user asked to regenerate the architecture diagram, do so and overwrite `images/{filename}`.

---

## Phase 5 — Report

Show the verification table and a diff-style summary of what changed.
