# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standardpage', '0024_auto_20171117_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardindex',
            name='social_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='social_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]