# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_auto_20170912_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_title', models.CharField(max_length=80)),
                ('partner_link', models.URLField(blank=True)),
                ('solution_summary', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]