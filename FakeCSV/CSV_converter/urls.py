from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data-schemas', views.DataSchemasView.as_view(), name='data_schemas'),
    path('data-schemas/new-schema', views.NewSchemaView.as_view(), name='new_schema'),
    path('data-sets/<str:name>/', views.DataSetsView.as_view(), name='data_sets'),
    path('edit-schema/<str:name>/', views.EditSchemaView.as_view(), name="edit_schema"),
]
