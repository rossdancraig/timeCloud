# Generated by Django 2.1.4 on 2018-12-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_recorder', '0007_auto_20181220_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
