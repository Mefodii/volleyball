# Generated by Django 2.1.2 on 2018-10-15 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20181005_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='payments',
        ),
    ]
