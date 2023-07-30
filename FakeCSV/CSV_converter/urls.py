from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data-schemas', login_required(views.DataSchemasView.as_view()), name='data_schemas'),
    path('data-schemas/new-schema', login_required(views.NewSchemaView.as_view()), name='new_schema'),
    path('data-sets/<str:name>/', login_required(views.DataSetsView.as_view()), name='data_sets'),
    path('edit-schema/<str:name>/', login_required(views.EditSchemaView.as_view()), name="edit_schema"),
]
