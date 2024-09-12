from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse

from faker import Faker

from CSV_converter.models import Schema, Column, IntegerColumn
from CSV_converter.views import get_email, generate_fake_data


class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        self.schema = Schema.objects.create(
            user=self.user,
            schema_name='TestSchema',
            column_separator=',',
            string_character='"'
        )
        self.column1 = Column.objects.create(
            name='ColumnName',
            type='1',
            order='1',
            schema=self.schema
        )
        self.column2 = Column.objects.create(
            name='ColumnName2',
            type='2',
            order='2',
            schema=self.schema
        )
        self.column3 = Column.objects.create(
            name='ColumnName3',
            type='3',
            order='3',
            schema=self.schema
        )
        self.column4 = IntegerColumn.objects.create(
            name='ColumnName4',
            type='4',
            order='4',
            schema=self.schema
        )
        self.column5 = Column.objects.create(
            name='ColumnName5',
            type='5',
            order='5',
            schema=self.schema
        )
        self.faker = Faker()

    def test_get_email_type(self):
        email = get_email(self.faker)
        self.assertIsInstance(email, str)

    def test_generate_fake_data_type(self):
        columns = [self.column1]
        fake_data = generate_fake_data(columns, self.faker)
        self.assertIsInstance(fake_data, list)

    def test_generate_fake_data_length_one_item(self):
        columns = [self.column1]
        fake_data = generate_fake_data(columns, self.faker)
        self.assertEqual(1, len(fake_data))

    def test_generate_fake_data_length_5_items(self):
        columns = [self.column1, self.column2,
                   self.column3, self.column4, self.column5]
        fake_data = generate_fake_data(columns, self.faker)
        self.assertEqual(5, len(fake_data))

    def test_data_schemas_view_get(self):
        url = reverse('data_schemas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_data_schemas_view_post_with_ajax(self):
        url = reverse('data_schemas')
        data = {
            'schema_id': '1',
        }
        response = self.client.post(
            url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
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
        # follow=True to follow redirects
        response = self.client.post(url, data, follow=True)
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
