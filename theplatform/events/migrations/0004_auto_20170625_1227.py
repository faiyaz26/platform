# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-25 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170625_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='datetime_from',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='datetime_to',
        ),
    ]
