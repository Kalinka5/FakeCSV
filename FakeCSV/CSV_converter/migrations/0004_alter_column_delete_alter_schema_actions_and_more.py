# Generated by Django 4.2.2 on 2023-06-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_converter', '0003_rename_column_name_column_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='delete',
            field=models.CharField(default='delete', max_length=255),
        ),
        migrations.AlterField(
            model_name='schema',
            name='actions',
            field=models.CharField(default='Edit scheme', max_length=255),
        ),
        migrations.AlterField(
            model_name='schema',
            name='modified',
            field=models.DateField(),
        ),
    ]
