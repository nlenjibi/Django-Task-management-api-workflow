from rest_framework.test import APITestCase
from rest_framework import status

class TaskAPITests(APITestCase):
    def test_list_empty(self):
        resp = self.client.get('/api/tasks/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        if isinstance(data, dict) and 'results' in data:
            self.assertEqual(data.get('count', 0), 0)
            self.assertEqual(data['results'], [])
        else:
            self.assertEqual(data, [])

    def test_create_task(self):
        payload = {"title":"Test Task","description":"A test task","completed":False}
        resp = self.client.post('/api/tasks/', payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        data = resp.json()
        self.assertEqual(data['title'], payload['title'])
        self.assertEqual(data['description'], payload['description'])
        self.assertEqual(data['completed'], payload['completed'])

    def test_retrieve_update_delete(self):
        create = self.client.post('/api/tasks/', {"title":"Test Task","description":"A test task"}, format='json')
        self.assertEqual(create.status_code, status.HTTP_201_CREATED)
        obj_id = create.json()['id']

        get = self.client.get(f'/api/tasks/{obj_id}/')
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(get.json()['title'], "Test Task")

        patch = self.client.patch(f'/api/tasks/{obj_id}/', {"completed": True}, format='json')
        self.assertEqual(patch.status_code, status.HTTP_200_OK)
        self.assertEqual(patch.json()['completed'], True)

        delete = self.client.delete(f'/api/tasks/{obj_id}/')
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_invalid(self):
        resp = self.client.post('/api/tasks/', {"description":"No title"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        data = resp.json()
        self.assertIn('title', data)
