# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0009_auto_20170905_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countrypage',
            old_name='context',
            new_name='introduction',
        ),
    ]
