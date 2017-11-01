# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('utils', '0004_statistic'),
        ('standardpage', '0010_auto_20171101_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardpagerelateddocument',
            name='document',
        ),
        migrations.RemoveField(
            model_name='standardpagerelateddocument',
            name='page',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedpage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedpage',
            name='source_page',
        ),
        migrations.AddField(
            model_name='standardpage',
            name='call_to_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.CallToActionSnippet'),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='hero_heading',
            field=models.CharField(blank=True, help_text='Heading that will appear over the hero image.', max_length=80),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage'),
        ),
        migrations.DeleteModel(
            name='StandardPageRelatedDocument',
        ),
        migrations.DeleteModel(
            name='StandardPageRelatedPage',
        ),
    ]
