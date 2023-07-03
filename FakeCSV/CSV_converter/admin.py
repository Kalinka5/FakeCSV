from django.contrib import admin

from CSV_converter.models import Schema, Column


admin.site.register(Schema)
admin.site.register(Column)
