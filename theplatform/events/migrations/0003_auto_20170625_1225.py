# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-25 11:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170625_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='datetime_from',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 25, 11, 25, 23, 21841, tzinfo=utc), verbose_name='Start datetime'),
        ),
    ]
