# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-17 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0029_auto_20171117_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleindex',
            name='introduction',
            field=models.TextField(blank=True, max_length=350),
        ),
    ]