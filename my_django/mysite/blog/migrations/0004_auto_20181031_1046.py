# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-31 10:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181031_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 10, 46, 47, 486595, tzinfo=utc)),
        ),
    ]
