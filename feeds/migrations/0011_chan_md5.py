# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20171128_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='chan',
            name='md5',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
