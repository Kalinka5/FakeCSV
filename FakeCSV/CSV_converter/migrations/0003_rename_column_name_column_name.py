# Generated by Django 4.2.2 on 2023-06-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_converter', '0002_column_schema_delete_columns_delete_dataschemas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='column_name',
            new_name='name',
        ),
    ]