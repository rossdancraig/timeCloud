# Generated by Django 2.1.4 on 2018-12-24 03:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event_recorder', '0011_auto_20181223_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 3, 19, 21, 420896, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 24, 2, 19, 21, 420858, tzinfo=utc)),
        ),
    ]
