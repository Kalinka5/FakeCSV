from django.contrib import admin

from CSV_converter.models import Schema, Column, File, Profile


admin.site.register(Profile)
admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(File)
