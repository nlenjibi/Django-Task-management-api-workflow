# Django Tasks API — Multi-stage AI Workflow

Problem Statement

- Design a multi-stage AI workflow that builds a Django REST API from scratch for an app named `tasks`. The `Task` model must include `title` (CharField), `description` (TextField), `completed` (BooleanField), and `created_at` (DateTimeField). Provide serializer, ViewSet, URLs, CRUD endpoints, structured JSON test cases, conversion of JSON tests into Django `TestCase` code, an ASCII workflow diagram, and the exact prompts used in each stage. Use at least two AI UX types and chain outputs between stages.

Tools Used

- Chat AI: planning, spec, test case generation, review
- IDE AI: generate source files (`models.py`, `serializers.py`, `views.py`, `urls.py`, `tests.py`, project settings, README)
- CLI AI: install deps, run migrations, execute tests

Step-by-Step Workflow

1. Stage 1 — Chat AI (Plan & scaffold spec)
   - Output: machine-readable scaffold spec (project name, app name, fields, endpoints, packages).
   - Chain: Pass spec to IDE AI.
2. Stage 2 — IDE AI (Code generation)
   - Input: scaffold spec.
   - Output: project skeleton and `tasks` app files: `tasks/models.py`, `tasks/serializers.py`, `tasks/views.py`, `tasks/urls.py`, `project/settings.py`, `project/urls.py`, `manage.py`, `requirements.txt`, `README.md`.
   - Chain: Files saved to workspace; pass instructions to CLI AI.
3. Stage 3 — CLI AI (Setup & run)
   - Input: project files and `requirements.txt`.
   - Output: results of venv creation, pip install, `makemigrations`, `migrate`, runserver or test outputs.
   - Chain: Feed runtime errors to IDE AI for fixes.
4. Stage 4 — Chat AI (Generate JSON test cases)
   - Input: API spec and serializers/views.
   - Output: structured JSON test cases describing CRUD operations (saved as `tests.json`).
   - Chain: Pass JSON to IDE AI.
5. Stage 5 — IDE AI (Convert JSON -> Django TestCase)
   - Input: `tests.json`.
   - Output: `tasks/tests.py` implementing `APITestCase` methods for each JSON test.
   - Chain: Send tests to CLI AI.
6. Stage 6 — CLI AI (Run tests)
   - Input: `python manage.py test tasks`.
   - Output: test runner results; loop until all pass.

Prompts for Each Tool (exact)

Stage 1 — Chat AI (Planning prompt)
"You are an expert backend architect. Design a minimal Django REST API scaffold for a project that includes a Django app named `tasks`. The `Task` model must include: `title` (CharField), `description` (TextField), `completed` (BooleanField default False), and `created_at` (DateTimeField auto_now_add=True). List required packages (including Django and Django REST framework), project layout (files to create), minimal `settings.py` changes to enable the app and REST framework, and the API endpoint design (endpoint paths, HTTP methods for CRUD). Produce the output in a machine-readable checklist format suitable for an IDE AI to consume."

Stage 2 — IDE AI (Code generation prompt)
"Using this scaffold spec (paste below), generate the complete contents for the following files for a Django 4+ project named `project` with an app `tasks`: `tasks/models.py`, `tasks/serializers.py`, `tasks/views.py`, `tasks/urls.py`, `project/urls.py` additions, `requirements.txt`, and a short `README.md` with exact CLI commands to set up the virtualenv, install deps, apply migrations, and run server. Ensure the `Task` model, a `TaskSerializer`, a `TaskViewSet` (ModelViewSet), router-based URLs at `/api/tasks/`, and basic permission (AllowAny) are included. Output each file separated and labeled with the filename."

Stage 3 — CLI AI (Execution prompt)
"Run these commands in sequence in a Windows PowerShell environment in the repo root. Show outputs and any errors:

1. `python -m venv .venv`
2. `.\.venv\Scripts\Activate.ps1`
3. `pip install -r requirements.txt`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python manage.py runserver --noreload --nothreading`
   If migrations fail, return error trace for IDE AI to fix files. Only proceed to runserver if migrations succeed."

Stage 4 — Chat AI (JSON test generation prompt)
"Produce structured JSON test cases for the `Task` CRUD API at `/api/tasks/`. The structure must be an array of test objects with these fields: `name`, `method`, `url`, `payload` (or null), `expected_status`, `expected_response` (partial match), and `notes`. Provide tests for: list (empty), create, retrieve, update (patch), delete, and create invalid (missing title). Keep sample data deterministic."

Stage 5 — IDE AI (Convert JSON -> Django TestCase prompt)
"Convert the following JSON test cases (paste below) into a Django test module `tasks/tests.py` using `rest_framework.test.APITestCase`. For each test case, create a test method that issues the request, asserts the `expected_status`, and verifies `expected_response` fields are present and equal when specified. Use the Django test client `self.client` (from DRF). Provide the complete `tasks/tests.py` content."

Stage 6 — CLI AI (Run tests prompt)
"Activate the venv and run `python manage.py test tasks`. Return the test runner output (pass/fail and tracebacks). If failures occur, include failing assertions and stack traces for IDE AI to repair code/tests."

Workflow Diagram (ASCII flowchart)

```
Start
  |
  v
[Stage 1: Chat AI — Plan & Spec]
  |
  v
[Scaffold Spec JSON]
  |
  v
[Stage 2: IDE AI — Generate code files]
  |
  v
[Project files: models, serializers, views, urls, requirements]
  |
  v
[Stage 3: CLI AI — Run setup & migrations]
  |
  v
[DB + server ready / errors -> back to IDE AI]
  |
  v
[Stage 4: Chat AI — Generate JSON test cases]
  |
  v
[JSON testcases]
  |
  v
[Stage 5: IDE AI — Convert JSON -> tests.py]
  |
  v
[tests.py]
  |
  v
[Stage 6: CLI AI — Run tests]
  |
  v
[Pass/Fail -> fix loop until pass]
  |
  v
End (Deliverables)
```

Expected Final Output

- Runnable Django project scaffold with app `tasks` and files:
  - `tasks/models.py` (Task model)
  - `tasks/serializers.py` (TaskSerializer)
  - `tasks/views.py` (TaskViewSet)
  - `tasks/urls.py` (router registration)
  - `project/urls.py` updated to include `api/` routes
  - `requirements.txt` with `Django` and `djangorestframework`
  - `tasks/tests.py` (DRF `APITestCase`) derived from JSON testcases

# AI-Powered Multi-Stage Workflow for Automated Django API Test Generation

Project Title

- AI-Powered Multi-Stage Workflow for Automated Django API Test Generation

Problem Statement

- Writing Django REST Framework API tests is repetitive, time-consuming, and error-prone. This workflow automates test generation using two AI UX types: Chat AI (for structured test-case design) and IDE AI (for converting JSON test specs into executable `tests.py`). A CLI stage runs and validates the generated tests.

Tools Used

- Tool 1 — Chat AI (ChatGPT): generate structured JSON test-case specifications.
- Tool 2 — IDE AI (Copilot / Cursor): convert JSON into a `tasks/tests.py` module using DRF testing best practices.
- Optional Tool 3 — CLI: run `python manage.py test` to validate.

Workflow (Overview)

1. Stage 1 — Test Design Agent (Chat AI)
   - Input: brief about `Task` API (fields and endpoints).
   - Output: structured JSON following schema `{"test_cases": [ ... ]}`.
   - Example ChatGPT prompt included below.
2. Stage 2 — Code Generation Agent (IDE AI)
   - Input: the JSON produced by Chat AI.
   - Output: `tasks/tests.py` containing an `APITestCase` class with one test method per JSON test case.
   - Example Copilot prompt included below.
3. Stage 3 — Validation (CLI)
   - Input: generated `tasks/tests.py` in workspace.
   - Action: run `python manage.py test` and iterate on failures.

Exact Prompts

Stage 1 — Chat AI (ChatGPT) prompt (use this verbatim):
"You are a senior QA automation engineer.\n\nGenerate structured API test cases for a Django REST Framework Task API.\n\nModel:\n- title (string, required, max_length=200)\n- description (string, optional)\n- completed (boolean, default=False)\n- created_at (auto-generated)\n\nEndpoints:\n- POST /api/tasks/\n- GET /api/tasks/\n- GET /api/tasks/{id}/\n- PUT /api/tasks/{id}/\n- DELETE /api/tasks/{id}/\n\nReturn test cases strictly in JSON format:\n\n{\n "test_cases": [\n {\n "name": "",\n "method": "",\n "endpoint": "",\n "payload": {},\n "expected_status": ,\n "expected_response_contains": []\n }\n ]\n}\n\nInclude tests: Valid task creation, Missing title, List tasks, Retrieve single task, Update task, Delete task, Invalid ID retrieval.\n\nKeep sample data deterministic."

Stage 2 — IDE AI (Copilot) prompt (use this verbatim):
"Using the following JSON test case specification, generate a Django REST Framework `tasks/tests.py` file.\n\nRequirements:\n- Use `rest_framework.test.APITestCase`\n- Use `reverse()` where possible\n- Dynamically create test data when needed\n- Follow DRF testing best practices\n- Each JSON test case becomes a `test_` method\n\nJSON Input:\n<PASTE JSON HERE>\n\nOutput: full `tasks/tests.py` content only."

Stage 3 — CLI (validation):
Run:

```
python manage.py test tasks
```

If failures occur, collect the error and use this debug prompt with ChatGPT or IDE AI:
"Analyze this Django test error:\n<PASTE ERROR>\nExplain: 1) Root cause 2) Exact fix 3) Corrected test code"

Sample JSON schema and example output (what ChatGPT must return)

```
{
  "test_cases": [
    {
      "name": "Create Task Successfully",
      "method": "POST",
      "endpoint": "/api/tasks/",
      "payload": {"title": "Test Task", "description": "Test Description"},
      "expected_status": 201,
      "expected_response_contains": ["id", "title", "completed"]
    },
    {
      "name": "Create Task Missing Title",
      "method": "POST",
      "endpoint": "/api/tasks/",
      "payload": {"description": "No title"},
      "expected_status": 400,
      "expected_response_contains": ["title"]
    }
    /* ...more cases... */
  ]
}
```

Workflow Diagram

```
[Existing Django Task API]
              ↓
[Chat AI]
  → Generates Structured JSON Test Cases
              ↓
(JSON Output Passed)
              ↓
[IDE AI]
  → Converts JSON → tests.py
              ↓
[Run manage.py test]
              ↓
[Automated Working Tests]
```

Video Script (3-minute demo)

- Show existing `Task` API briefly.\n- Run ChatGPT prompt and copy JSON output.\n- Paste into Copilot / IDE and generate `tasks/tests.py`.\n- Run `python manage.py test` and show passing tests.\n
  Why this approach is strong
- Focused: targets testing automation only.\n+- Demonstrable: small surface and fast feedback loop.\n+- Reusable: same pattern applies to other DRF resources.

Files to update in this workspace

- `WORKFLOW.md` (this file) — updated
- `README.md` — updated to reflect project focus
- `tests.json` — sample JSON used as input to IDE AI

Repository status

- `scripts/generate_tests_from_json.py` — generator script that converts `tests.json` into `tasks/tests_auto.py`.
- `tests.json` — structured JSON test-case specification (source of truth for generation).
- `tasks/tests_auto.py` — generated test module (created by the generator).
- `tasks/tests.py` — optional hand-written tests (kept for reference).
- `WORKFLOW.md`, `README.md`, `.gitignore` — docs and repo settings.

Recommended workflow (current)

1. Activate the project virtual environment.

```powershell
.\.venv\Scripts\Activate.ps1
```

2. Generate tests from the JSON specification.

```powershell
python .\scripts\generate_tests_from_json.py
```

3. Review `tasks/tests_auto.py`. If you prefer the generated tests as canonical tests, either:

- Replace or merge into `tasks/tests.py` (recommended for a single authoritative test file), or
- Keep `tasks/tests_auto.py` separate and ignore it in CI if you want manual tests only.

4. Run the Django test suite and iterate on failures.

```powershell
python manage.py test tasks
```

5. Commit the generator and reviewed/generated tests.

```powershell
git add scripts/generate_tests_from_json.py tests.json tasks/tests_auto.py WORKFLOW.md README.md
git commit -m "chore(tests): add generator and generated API tests"
```

Notes

- The generator emits DRF `APITestCase` tests using `reverse('task-list')` and `reverse('task-detail')` where applicable.
- Generated tests passed locally in the project venv at the time of creation.
- You can customize `tests.json` to add more cases and re-run the generator to update `tasks/tests_auto.py`.

Generator usage

Run the generator and tests (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
python .\scripts\generate_tests_from_json.py
python manage.py test tasks
```

Commit generator and generated tests:

```powershell
git add scripts/generate_tests_from_json.py tests.json tasks/tests_auto.py WORKFLOW.md README.md
git commit -m "chore: add test generator and generated tests"
```
