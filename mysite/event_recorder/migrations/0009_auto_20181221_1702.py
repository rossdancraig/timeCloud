# Generated by Django 2.1.4 on 2018-12-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_recorder', '0008_event_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
