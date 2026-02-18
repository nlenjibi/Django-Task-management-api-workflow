# Multi-Stage AI Workflow: Automated Django API Test Generation

## 1. Problem Statement

Writing automated tests for Django REST Framework (DRF) APIs is repetitive and time-consuming. Developers must manually:

- Analyze API endpoints
- Design test cases
- Write structured test methods
- Validate expected responses
- Handle edge cases

This project asks: How can we automate Django API test design and implementation using a structured multi-stage AI workflow to reduce manual effort while keeping high-quality, structured test coverage?

## 2. Tools Used

This workflow integrates two AI UX types:

1. Chat AI (ChatGPT)
   - Generates structured API test case specifications in JSON.
2. IDE AI (GitHub Copilot / Cursor)
   - Converts the structured JSON test cases into executable `tests.py` code.

The output from Chat AI becomes the input to the IDE AI, forming a chained workflow.

## 3. Step-by-Step Workflow Instructions

### Stage 1 — Generate Structured Test Cases (Chat AI)

Step 1: Provide the Task API specification to ChatGPT.

Prompt (example):

```
Generate structured API test cases for a Django REST Framework Task API.

Model:
- title (string, required, max_length=200)
- description (string, optional)
- completed (boolean, default=False)
- created_at (auto-generated)

Endpoints:
- POST /api/tasks/
- GET /api/tasks/
- GET /api/tasks/{id}/
- PUT /api/tasks/{id}/
- DELETE /api/tasks/{id}/

Return test cases strictly in JSON format:

{
  "test_cases": [
    {
      "name": "",
      "method": "",
      "endpoint": "",
      "payload": {},
      "expected_status": ,
      "expected_response_contains": []
    }
  ]
}

Include:
- Valid task creation
- Missing title
- List tasks
- Retrieve single task
- Update task
- Delete task
- Invalid ID retrieval
```

Save the JSON output (e.g., `tests.json`). This JSON is the single source of truth for test generation.

### Stage 2 — Convert JSON into Django Tests (IDE AI)

Step 2: Use Copilot or Cursor inside VS Code. Paste the JSON and instruct the IDE AI to generate `tasks/tests.py`.

IDE prompt (example):

```
Using the generated JSON test case specification, generate a Django REST Framework tests.py file.

Requirements:
- Use `APITestCase`.
- Use `reverse()` where possible.
- Dynamically create test data using the `Task` model.
- Follow DRF best practices:
  - Use `rest_framework.status` for status codes.
  - Use `format='json'` in client requests.
- Convert each JSON test case into a separate test method.
- Name methods by converting the test case name to snake_case. Example: "List empty tasks" → `test_list_empty_tasks`.
- For list endpoints:
  - If `response.data` is a dict, assert it contains a `results` key and validate `response.data["results"]`.
  - Otherwise treat `response.data` as a plain list and validate it directly.
- Include concise assertions for status codes and expected response fields from the JSON spec.

Output:
- Fully structured `tests.py` with multiple test methods, proper DRF test client usage, and automated coverage for all endpoints.
```

Notes:

- Keep test methods small and focused on a single behavior.
- Use fixtures or factory methods to make tests readable and maintainable.

### Stage 3 — Execute and Validate

Run tests locally:

```bash
python manage.py test
```

Green tests confirm the end-to-end workflow from JSON spec → generated tests → executed assertions.

## 4. Workflow Diagram (Data Flow)

[Existing Django Task API]
↓
[Chat AI]
→ Generate Structured JSON Test Cases
↓
(JSON Test Case Specification)
↓
[IDE AI]
→ Convert JSON into tests.py
↓
[Automated Django Test File Generated]
↓
[Run manage.py test]
↓
[Working Automated Tests]

## 5. Efficiency Gains

- Eliminates manual test case design
- Automates repetitive test method creation
- Standardizes test structure
- Reduces human error

Estimated time savings: 50–70% compared to writing tests manually.

## 6. Adaptability

This workflow applies to any REST API (Django, Flask, FastAPI, microservices). The key principle is structured data handoff (JSON → Code Generation).

## 7. Proof of Execution

Suggested artifacts to include for submission:

- Screenshot 1: ChatGPT generating JSON test cases (`assets/screenshots/chatgpt-json.png`)
- Screenshot 2: JSON pasted into IDE (`assets/screenshots/ide-paste-json.png`)
- Screenshot 3: Copilot generating `tests.py` (`assets/screenshots/copilot-tests.png`)
- Screenshot 4: Terminal showing successful `python manage.py test` (`assets/screenshots/test-success.png`)
- `tests.json` — the generated JSON used as input

Alternatively, record a 2–3 minute video demonstrating the handoff and successful test run.

## 8. Conclusion

This project demonstrates a functional multi-stage AI workflow that chains:

Chat AI → Structured Test Design

IDE AI → Automated Test Implementation

It reduces manual effort while producing structured, maintainable tests.

---

