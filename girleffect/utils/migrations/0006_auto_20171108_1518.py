# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_auto_20171102_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='statistic_units',
            field=models.CharField(blank=True, help_text="The units of the statistic (e.g. the '%' in '85%')", max_length=4, null=True, verbose_name='Units'),
        ),
    ]
