import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TEST_JSON = BASE / 'tests.json'
OUT_FILE = BASE / 'tasks' / 'tests_auto.py'

def slug(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9_]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = 'case'
    return s

template_header = '''from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class GeneratedTaskAPITests(APITestCase):
'''

def gen_test_case(tc: dict) -> str:
    name = tc.get('name', 'case')
    method = tc.get('method', 'GET').upper()
    endpoint = tc.get('endpoint', '')
    payload = tc.get('payload')
    exp_status = tc.get('expected_status')
    expected_keys = tc.get('expected_response_contains', []) or []

    fn_name = 'test_' + slug(name)
    lines = [f'    def {fn_name}(self):']

    # If endpoint uses {id}, create an object first
    if '{id}' in endpoint:
        lines.append("        # create a task to use its id")
        lines.append("        create_resp = self.client.post(reverse('task-list'), {'title': 'Auto Task', 'description': 'generated'}, format='json')")
        lines.append("        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)")
        lines.append("        obj_id = create_resp.json().get('id')")
        ep = endpoint.replace('{id}', "{obj_id}")
        # build request URL using reverse when possible
        lines.append("        url = reverse('task-detail', args=[obj_id])")
    else:
        if endpoint.endswith('/') and endpoint.count('/') == 3:
            # likely list endpoint /api/tasks/
            lines.append("        url = reverse('task-list')")
        else:
            lines.append(f"        url = '{endpoint}'")

    # Perform request
    if method == 'GET':
        lines.append("        resp = self.client.get(url)")
    elif method == 'POST':
        if payload is None:
            lines.append("        resp = self.client.post(url, {}, format='json')")
        else:
            lines.append(f"        resp = self.client.post(url, {repr(payload)}, format='json')")
    elif method == 'PATCH':
        lines.append(f"        resp = self.client.patch(url, {repr(payload or {})}, format='json')")
    elif method == 'PUT':
        lines.append(f"        resp = self.client.put(url, {repr(payload or {})}, format='json')")
    elif method == 'DELETE':
        lines.append("        resp = self.client.delete(url)")
    else:
        lines.append("        # unsupported method in generator")

    lines.append(f"        self.assertEqual(resp.status_code, {exp_status})")

    # If expected keys, assert presence when response has JSON
    if expected_keys and exp_status not in (204,):
        lines.append("        try:")
        lines.append("            data = resp.json()")
        lines.append("        except ValueError:")
        lines.append("            data = None")
        lines.append("        if isinstance(data, dict):")
        for k in expected_keys:
            lines.append(f"            self.assertIn('{k}', data)")
    lines.append("")
    return '\n'.join(lines)

def main():
    raw = json.loads(TEST_JSON.read_text())
    cases = raw.get('test_cases', [])
    out = [template_header]
    for tc in cases:
        out.append(gen_test_case(tc))

    OUT_FILE.write_text('\n'.join(out))
    print(f'Wrote {OUT_FILE}')

if __name__ == '__main__':
    main()
