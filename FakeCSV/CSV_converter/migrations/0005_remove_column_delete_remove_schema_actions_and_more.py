# Generated by Django 4.2.2 on 2023-07-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_converter', '0004_alter_column_delete_alter_schema_actions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='actions',
        ),
        migrations.AddField(
            model_name='column',
            name='from_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='column',
            name='to_field',
            field=models.IntegerField(default=0),
        ),
    ]