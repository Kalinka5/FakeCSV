from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from CSV_converter.forms import SchemaForm
from CSV_converter.models import Profile

from members.forms import NewUserForm, ProfileForm, ProfileImgForm, PasswordChangingForm

import os

class FormTests(TestCase):
    def test_schema_form_valid(self):
        data = {
            'schema_name': 'Test Schema',
            'column_separator': ',',
            'string_character': '"'
        }
        form = SchemaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_schema_form_invalid(self):
        # Test with missing required fields or invalid data
        data = {
            'schema_name': '',  # Missing required field
            'column_separator': ',',
            'string_character': 123  # Invalid data
        }
        form = SchemaForm(data=data)
        self.assertFalse(form.is_valid())

    def test_new_user_form_valid(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = NewUserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_new_user_form_invalid(self):
        # Test with missing required fields or invalid data
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword'  # Passwords don't match
        }
        form = NewUserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_profile_form_valid(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        data = {
            'email': 'updated@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser'
        }
        form = ProfileForm(instance=user, data=data)
        self.assertTrue(form.is_valid())

    def test_profile_img_form_valid(self):
        profile = Profile.objects.create(user=User.objects.create_user(username='testuser'))

        root_folder = os.getcwd()
        image_path = os.path.join(root_folder, 'tests', 'test_images', 'jpg_image.jpg')

        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            
        image = SimpleUploadedFile("jpg_image.jpg", image_data, content_type="image/jpeg")
        data = {'picture': image}

        form = ProfileImgForm(instance=profile, data=data, files=data)
        self.assertTrue(form.is_valid())

    def test_password_changing_form_valid(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')
        
        data = {
            'old_password': 'testpassword123',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123'
        }
        form = PasswordChangingForm(user=user, data=data)
        self.assertTrue(form.is_valid())

    def test_password_changing_form_invalid(self):
        user = User.objects.create_user(username='testuser')
        data = {
            'old_password': 'wrongpassword',  # Incorrect old password
            'new_password1': 'newpassword123',
            'new_password2': 'mismatchedpassword'  # Passwords don't match
        }
        form = PasswordChangingForm(user=user, data=data)
        self.assertFalse(form.is_valid())
