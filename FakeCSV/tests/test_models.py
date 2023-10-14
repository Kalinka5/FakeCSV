from django.test import TestCase
from django.contrib.auth.models import User

import datetime

from CSV_converter.models import Schema, Column, IntegerColumn, File, Profile

class TestModels(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.schema1 = Schema.objects.create(
            user=self.user,
            schema_name='Test Schema with comma and double quotes',
            column_separator=',',
            string_character='"'
        )
        self.schema2 = Schema.objects.create(
            user=self.user,
            schema_name='Test Schema with semicolon and single quotes',
            column_separator=';',
            string_character="'"
        )
        self.column = Column.objects.create(
            name='Test Column',
            type='1',
            order='1',
            schema=self.schema1
        )
        self.integer_column = IntegerColumn.objects.create(
            name='Integer Test Column',
            type='4',
            order='2',
            schema=self.schema1,
            range_low=20,
            range_high=50
        )
        self.file = File.objects.create(
            name='Test File',
            schema=self.schema1
        )
        self.profile = Profile.objects.create(
            user=self.user
        )

    def test_schema_model_with_comma_double_quotes(self):
        schema = Schema.objects.get(schema_name='Test Schema with comma and double quotes')
        self.assertEqual(schema.user, self.user)
        self.assertEqual(schema.schema_name, 'Test Schema with comma and double quotes')
        self.assertEqual(schema.column_separator, ',')
        self.assertEqual(schema.string_character, '"')
        self.assertEqual(schema.modified, datetime.date.today())

    def test_schema_model_with_semicolon_single_quotes(self):
        schema = Schema.objects.get(schema_name='Test Schema with semicolon and single quotes')
        self.assertEqual(schema.user, self.user)
        self.assertEqual(schema.schema_name, 'Test Schema with semicolon and single quotes')
        self.assertEqual(schema.column_separator, ';')
        self.assertEqual(schema.string_character, "'")
        self.assertEqual(schema.modified, datetime.date.today())

    def test_column_model(self):
        column = Column.objects.get(name='Test Column')
        self.assertEqual(column.name, 'Test Column')
        self.assertEqual(column.type, '1')
        self.assertEqual(column.order, '1')
        self.assertEqual(column.schema, self.schema1)

    def test_integer_column_model(self):
        integer_column = IntegerColumn.objects.get(name='Integer Test Column')
        self.assertEqual(integer_column.name, 'Integer Test Column')
        self.assertEqual(integer_column.type, '4')
        self.assertEqual(integer_column.order, '2')
        self.assertEqual(integer_column.schema, self.schema1)
        self.assertEqual(integer_column.range_low, 20)
        self.assertEqual(integer_column.range_high, 50)

    def test_integer_column_model_default_range_low_high(self):
        integer_column = IntegerColumn.objects.create(
            name='Integer Test Column Default Range Low And High',
            type='3',
            order='3',
            schema=self.schema1
        )
        self.assertEqual(integer_column.range_low, 0)
        self.assertEqual(integer_column.range_high, 100)    

    def test_file_model(self):
        file = File.objects.get(name='Test File')
        self.assertEqual(file.name, 'Test File')
        self.assertEqual(file.date, datetime.date.today())
        self.assertEqual(file.schema, self.schema1)

    def test_profile_model(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)
        self.assertFalse(bool(profile.picture))

    def test_schema_str_method(self):
        schema = Schema.objects.get(schema_name='Test Schema with comma and double quotes')
        self.assertEqual(str(schema), 'Test Schema with comma and double quotes')

    def test_column_str_method(self):
        column = Column.objects.get(name='Test Column')
        self.assertEqual(str(column), 'Test Column')

    def test_integer_column_str_method(self):
        integer_column = IntegerColumn.objects.get(name='Integer Test Column')
        self.assertEqual(str(integer_column), 'Integer Test Column')

    def test_file_str_method(self):
        file = File.objects.get(name='Test File')
        self.assertEqual(str(file), 'Test File')

    def test_profile_str_method(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser')
