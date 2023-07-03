from django.urls import path
from . import views

urlpatterns = [
    path('data-schemas', views.data_schemas, name='data_schemas'),
    path('data-schemas/new-schema', views.new_schema, name='new_schema'),
    path('data-sets', views.data_sets, name='data_sets'),
]
