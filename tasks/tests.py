from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task


class TaskAPITests(APITestCase):
	def test_list_empty_tasks(self):
		"""List empty tasks"""
		Task.objects.all().delete()
		url = reverse('task-list')
		resp = self.client.get(url, format='json')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)

		data = resp.data
		if isinstance(data, dict):
			self.assertIn('results', data)
			self.assertEqual(data['results'], [])
		else:
			self.assertEqual(data, [])

	def test_create_task(self):
		"""Create task"""
		url = reverse('task-list')
		payload = {"title": "Test Task", "description": "A test task", "completed": False}
		resp = self.client.post(url, payload, format='json')
		self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

		# Assert expected fields present
		for field in ("id", "title", "completed"):
			self.assertIn(field, resp.data)

		# Verify stored in DB
		task = Task.objects.get(pk=resp.data['id'])
		self.assertEqual(task.title, payload['title'])
		self.assertEqual(task.completed, payload['completed'])

	def test_retrieve_task(self):
		"""Retrieve task"""
		task = Task.objects.create(title='Retrieve me', description='x', completed=False)
		url = reverse('task-detail', args=[task.id])
		resp = self.client.get(url, format='json')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertIn('title', resp.data)
		self.assertEqual(resp.data['title'], task.title)

	def test_partial_update_task(self):
		"""Partial update task"""
		task = Task.objects.create(title='To update', description='', completed=False)
		url = reverse('task-detail', args=[task.id])
		payload = {"completed": True}
		resp = self.client.patch(url, payload, format='json')
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertIn('completed', resp.data)
		self.assertTrue(resp.data['completed'])

		task.refresh_from_db()
		self.assertTrue(task.completed)

	def test_delete_task(self):
		"""Delete task"""
		task = Task.objects.create(title='To delete', description='', completed=False)
		url = reverse('task-detail', args=[task.id])
		resp = self.client.delete(url, format='json')
		self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Task.objects.filter(pk=task.id).exists())

	def test_create_invalid_missing_title(self):
		"""Create invalid (missing title)"""
		url = reverse('task-list')
		payload = {"description": "No title"}
		resp = self.client.post(url, payload, format='json')
		self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
		# Validation error should reference the missing 'title' field
		self.assertIn('title', resp.data)

	def test_retrieve_invalid_id(self):
		"""Retrieve invalid ID"""
		# Use an ID that does not exist
		url = reverse('task-detail', args=[9999])
		resp = self.client.get(url, format='json')
		self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

