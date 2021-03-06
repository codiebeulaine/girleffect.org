# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_auto_20170811_1305'),
        ('countries', '0008_auto_20170830_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrypagerelatedsolution',
            name='source_page',
        ),
        migrations.AddField(
            model_name='countrypagerelatedsolution',
            name='solution_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_solutions', to='solutions.SolutionPage'),
        ),
        migrations.AlterField(
            model_name='countrypagerelatedsolution',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='countries.CountryPage'),
        ),
    ]
