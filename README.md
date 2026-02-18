# AI-Powered Multi-Stage Workflow for Automated Django API Test Generation

This project demonstrates an AI-assisted workflow that automates writing Django REST Framework tests for an existing `tasks` API. It focuses on three stages:

- Stage 1 — Chat AI: produce a structured JSON test-case specification.
- Stage 2 — IDE AI: convert the JSON into `tasks/tests.py` (DRF `APITestCase`).
- Stage 3 — CLI: run `python manage.py test` to validate.

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

Files of interest:

- `WORKFLOW.md` — exact prompts and workflow description
- `tests.json` — example JSON test specification
- `tasks/tests.py` — generated test file (may be overwritten by IDE AI output)
