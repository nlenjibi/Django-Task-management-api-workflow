# AI-Powered Multi-Stage Workflow for Automated Django API Test Generation

````markdown
# AI-Powered Multi-Stage Workflow for Automated Django API Test Generation

This project demonstrates an AI-assisted workflow that automates writing Django REST Framework tests for an existing `tasks` API. It focuses on three stages:

- Stage 1 — Chat AI: produce a structured JSON test-case specification.
- Stage 2 — IDE AI: convert the JSON into `tasks/tests.py` (DRF `APITestCase`).

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Run tests:

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py test tasks
```

How to use the AI workflow (summary):

1. Run the ChatGPT prompt (see `WORKFLOW.md`) to generate a JSON spec.
2. Paste JSON into your IDE AI (Copilot/Cursor) with the provided prompt to generate `tasks/tests.py`.
3. Run `python manage.py test tasks` and iterate until green.

Documentation and artifacts:

- `WORKFLOW.md` — full workflow, prompts, and examples (new)
- `docs/AI_Test_Workflow.docx` — downloadable Word copy (placeholder)
- `assets/screenshots/` — example screenshot filenames used in the project
- `tests.json` — example JSON test specification
- `tasks/tests.py` — generated test file (may be overwritten by IDE AI output)

See the full workflow document at [WORKFLOW.md](WORKFLOW.md).
````
