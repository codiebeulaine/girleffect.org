# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171115_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_strapline',
            field=models.TextField(help_text='Shows text over the hero.', max_length=80),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='link_page',
            field=models.ForeignKey(blank=True, help_text='Optional page link as clickthrough for hero video.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Page Link'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='link_youtube',
            field=models.URLField(blank=True, help_text='Optional URL for a full length YouTube video goes here,                    which will open in a modal window.', verbose_name='YouTube Link'),
        ),
    ]
