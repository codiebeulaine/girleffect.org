# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171107_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='strapline',
            new_name='hero_strapline',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='link_url',
        ),
        migrations.AddField(
            model_name='homepage',
            name='link_youtube',
            field=models.URLField(blank=True, help_text='Optional URL for a full length YouTube video goes here,                    which will open in a modal window.'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_video',
            field=models.ForeignKey(blank=True, help_text='Short Hero Video to show on top of page. Recommended size 12Mb or under.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='link_page',
            field=models.ForeignKey(blank=True, help_text='Optional page link as clickthrough for hero video.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
