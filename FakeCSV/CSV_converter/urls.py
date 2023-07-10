from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('data-schemas', views.data_schemas, name='data_schemas'),
    path('data-schemas/new-schema', views.new_schema, name='new_schema'),
    path('data-sets/<str:name>/', views.DataSetsView.as_view(), name='data_sets'),
    path('edit-schema/<str:name>/', views.edit_schema, name="edit_schema"),
]
