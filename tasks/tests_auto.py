from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class GeneratedTaskAPITests(APITestCase):

    def test_list_empty_tasks(self):
        url = reverse('task-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        try:
            data = resp.json()
        except ValueError:
            data = None
        if isinstance(data, dict):
            self.assertIn('results', data)

    def test_create_task(self):
        url = reverse('task-list')
        resp = self.client.post(url, {'title': 'Test Task', 'description': 'A test task', 'completed': False}, format='json')
        self.assertEqual(resp.status_code, 201)
        try:
            data = resp.json()
        except ValueError:
            data = None
        if isinstance(data, dict):
            self.assertIn('id', data)
            self.assertIn('title', data)
            self.assertIn('completed', data)

    def test_retrieve_task(self):
        # create a task to use its id
        create_resp = self.client.post(reverse('task-list'), {'title': 'Auto Task', 'description': 'generated'}, format='json')
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        obj_id = create_resp.json().get('id')
        url = reverse('task-detail', args=[obj_id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        try:
            data = resp.json()
        except ValueError:
            data = None
        if isinstance(data, dict):
            self.assertIn('title', data)

    def test_partial_update_task(self):
        # create a task to use its id
        create_resp = self.client.post(reverse('task-list'), {'title': 'Auto Task', 'description': 'generated'}, format='json')
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        obj_id = create_resp.json().get('id')
        url = reverse('task-detail', args=[obj_id])
        resp = self.client.patch(url, {'completed': True}, format='json')
        self.assertEqual(resp.status_code, 200)
        try:
            data = resp.json()
        except ValueError:
            data = None
        if isinstance(data, dict):
            self.assertIn('completed', data)

    def test_delete_task(self):
        # create a task to use its id
        create_resp = self.client.post(reverse('task-list'), {'title': 'Auto Task', 'description': 'generated'}, format='json')
        self.assertEqual(create_resp.status_code, status.HTTP_201_CREATED)
        obj_id = create_resp.json().get('id')
        url = reverse('task-detail', args=[obj_id])
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)

    def test_create_invalid_missing_title(self):
        url = reverse('task-list')
        resp = self.client.post(url, {'description': 'No title'}, format='json')
        self.assertEqual(resp.status_code, 400)
        try:
            data = resp.json()
        except ValueError:
            data = None
        if isinstance(data, dict):
            self.assertIn('title', data)

    def test_retrieve_invalid_id(self):
        url = '/api/tasks/9999/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
