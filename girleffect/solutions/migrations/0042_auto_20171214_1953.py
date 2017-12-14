# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('solutions', '0041_auto_20171214_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionpage',
            name='lower_background_image',
            field=models.ForeignKey(blank=True, help_text='Add an image to appear as background for page related articles', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage'),
        ),
        migrations.AddField(
            model_name='solutionpage',
            name='upper_background_image',
            field=models.ForeignKey(blank=True, help_text='Add an image to appear as background for page introduction', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage'),
        ),
    ]
