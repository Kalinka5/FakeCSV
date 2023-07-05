# Generated by Django 4.2.2 on 2023-07-05 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSV_converter', '0005_remove_column_delete_remove_schema_actions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegerColumn',
            fields=[
                ('column_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CSV_converter.column')),
                ('range_low', models.IntegerField(blank=True, default=0, null=True)),
                ('range_high', models.IntegerField(blank=True, default=100, null=True)),
            ],
            bases=('CSV_converter.column',),
        ),
        migrations.RemoveField(
            model_name='column',
            name='from_field',
        ),
        migrations.RemoveField(
            model_name='column',
            name='to_field',
        ),
    ]
