# Generated by Django 4.2.3 on 2023-07-18 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CSV_converter', '0007_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schema',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
