# Generated by Django 2.1.2 on 2018-10-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='payments',
            field=models.ManyToManyField(blank=True, to='accounting.Payment'),
        ),
    ]
