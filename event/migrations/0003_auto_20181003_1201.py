# Generated by Django 2.1.2 on 2018-10-03 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20181003_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voleibalist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Registered User'),
        ),
    ]
