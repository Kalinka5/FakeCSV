from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from CSV_converter.views import (
    DataSchemasView,
    NewSchemaView,
    DataSetsView,
    EditSchemaView,
    home
)

from members.views import (
    UserRegisterView,
    UserProfileView,
    update_user,
    DeleteUserView,
    PasswordsChangeView,
    password_success
)


class TestUrls(SimpleTestCase):

    def test_home_page_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_data_schemas_page_url_resolves(self):
        url = reverse('data_schemas')
        self.assertEqual(resolve(url).func.view_class, DataSchemasView)

    def test_create_new_schema_url_resolves(self):
        url = reverse('new_schema')
        self.assertEqual(resolve(url).func.view_class, NewSchemaView)

    def test_data_sets_page_url_resolves(self):
        url = reverse('data_sets', args=["New"])
        self.assertEqual(resolve(url).func.view_class, DataSetsView)

    def test_edit_schema_url_resolves(self):
        url = reverse('edit_schema', args=["New"])
        self.assertEqual(resolve(url).func.view_class, EditSchemaView)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)

    def test_get_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, UserProfileView)

    def test_edit_profile_url_resolves(self):
        url = reverse('edit_profile')
        self.assertEqual(resolve(url).func, update_user)

    def test_delete_account_url_resolves(self):
        url = reverse('account_delete')
        self.assertEqual(resolve(url).func.view_class, DeleteUserView)

    def test_change_password_url_resolves(self):
        url = reverse('change_password')
        self.assertEqual(resolve(url).func.view_class, PasswordsChangeView)

    def test_success_changed_password_url_resolves(self):
        url = reverse('password_success')
        self.assertEqual(resolve(url).func, password_success)

    def test_reset_password_url_resolves(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_done_url_resolves(self):
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_confirm_url_resolves(self):
        url = reverse('password_reset_confirm', args=[1, "123"])
        self.assertEqual(resolve(url).func.view_class,
                         PasswordResetConfirmView)

    def test_password_reset_complete_url_resolves(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class,
                         PasswordResetCompleteView)
