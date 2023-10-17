from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse

from CSV_converter.models import Schema, Column

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        self.schema = Schema.objects.create(
            user=self.user,
            schema_name='TestSchema',
            column_separator=',',
            string_character='"'
        )
        self.column = Column.objects.create(
            name='ColumnName',
            type='1',
            order='1',
            schema=self.schema
        )

    def test_data_schemas_view_get(self):
        url = reverse('data_schemas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_data_schemas_view_post_with_ajax(self):
        url = reverse('data_schemas')
        data = {
            'schema_id': '1',
        }
        response = self.client.post(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertIsInstance(response, JsonResponse)
        self.assertTrue(response.json()['success'])

    def test_data_schemas_view_post_without_ajax(self):
        url = reverse('data_schemas')
        data = {
            'schema_id': '1',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

    def test_new_schema_view_get(self):
        url = reverse('new_schema')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_schema_view_post(self):
        url = reverse('new_schema')
        data = {
            'schema_name': 'NewTestSchema',
            'column_separator': ',',
            'string_character': '"',
            'column_name': 'Test',
            'type': '1',
            'order': '1',
            'from[]': '10',
            'to[]': '70'
        }
        response = self.client.post(url, data, follow=True) # follow=True to follow redirects
        self.assertEqual(response.status_code, 200)

    def test_data_sets_view_get(self):
        url = reverse('data_sets', kwargs={'name': 'TestSchema'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_data_sets_view_post(self):
        url = reverse('data_sets', kwargs={'name': 'TestSchema'})
        data = {
            'rows': 10
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_edit_schema_view_get(self):
        url = reverse('edit_schema', kwargs={'name': 'TestSchema'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_schema_view_post(self):
        url = reverse('edit_schema', kwargs={'name': 'TestSchema'})
        data = {
            'submit': 'Submit',
            'schema_name': 'UpdatedSchemaName',
            'separator': ',',
            'character': '"',
            'column_name': 'Test',
            'type': '1',
            'order': '1',
            'from[]': '10',
            'to[]': '70'
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
