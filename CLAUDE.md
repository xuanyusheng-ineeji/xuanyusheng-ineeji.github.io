# Claude Code Instructions

## Adding a Project to the Portfolio

When the user says "add project [GitHub URL] to my portfolio", follow these steps:

1. **Fetch repo content** — read in order of priority:
   - `PROJECT_SUMMARY.md` (most concise, portfolio-ready)
   - `README.md` (fallback)
   - `CLAUDE.md` (additional context)

2. **Add an entry to `_data/projects.yml`** under `industry:` or `personal:` using this schema:
   ```yaml
   - title: "Project Name — One-line Tagline"
     org: "Organization · Team"          # omit if personal project
     github: "https://github.com/..."
     image: "/images/filename.png"       # generate or leave as placeholder
     badge: "Org · Year"
     description: >
       2–3 sentence summary of what the project does and its impact.
     bullets:
       - "**Key aspect**: detail"
       - "**Key aspect**: detail"
       - "**Key aspect**: detail"
       - "**Key aspect**: detail"
     tech: "Tech1 · Tech2 · Tech3"
   ```

3. **Generate architecture image** if no suitable image exists — save to `images/` and set the `image` field.

4. **Do not modify `_pages/projects.md`** — it auto-renders from the data file.

## Site Structure

- `_data/projects.yml` — project registry (source of truth)
- `_includes/project-card.html` — paper-box card template
- `_pages/projects.md` — auto-rendered projects page
- `_pages/about.md` — homepage content
- `_data/navigation.yml` — top navigation bar
- `images/` — all images (use absolute paths with leading `/`)
- `portfolio_assistant/` — RAG chatbot backend (FastAPI + LangChain + Ollama)

## Image Path Rule

Always use absolute paths starting with `/` for images:
- ✅ `/images/foo.png`
- ❌ `images/foo.png`

## Jekyll Dev Server

```powershell
$env:PATH = "C:\Ruby33-x64\bin;" + $env:PATH
bundle exec jekyll serve --livereload
```
