# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_solutionpage_call_to_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solutionpage',
            old_name='introduction',
            new_name='summary',
        ),
    ]
