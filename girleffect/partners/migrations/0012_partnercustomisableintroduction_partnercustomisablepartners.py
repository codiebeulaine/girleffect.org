# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('partners', '0011_auto_20171124_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerCustomisableIntroduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('background_hex', models.CharField(blank=True, max_length=7, null=True)),
                ('heading_hex', models.CharField(blank=True, max_length=7, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='introduction_customisation', to='partners.PartnerIndexPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='PartnerCustomisablePartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('background_hex', models.CharField(blank=True, max_length=7, null=True)),
                ('heading_hex', models.CharField(blank=True, max_length=7, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_customisation', to='partners.PartnerIndexPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
