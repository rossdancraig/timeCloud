# Generated by Django 2.1.4 on 2018-12-21 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_recorder', '0003_auto_20181220_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
    ]
