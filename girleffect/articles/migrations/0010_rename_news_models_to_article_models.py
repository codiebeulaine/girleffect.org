# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import girleffect.utils.models
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import girleffect.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('utils', '0003_auto_20171017_1044'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('images', '0001_initial'),
        ('articles', '0009_rename_news_tables_and_contenttypes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsPage',
            new_name='ArticlePage',
        ),
        migrations.RenameModel(
            old_name='NewsIndex',
            new_name='ArticleIndex',
        ),
        migrations.RenameModel(
            old_name='NewsPageCategory',
            new_name='ArticlePageCategory',
        ),
        migrations.RenameModel(
            old_name='NewsPageRelatedDocument',
            new_name='ArticlePageRelatedDocument',
        ),
        migrations.RenameModel(
            old_name='NewsPageRelatedPage',
            new_name='ArticlePageRelatedPage',
        ),
        migrations.AlterField(
            model_name='articlepagecategory',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='articles.ArticlePage'),
        ),
        migrations.AlterField(
            model_name='articlepagerelateddocument',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_documents', to='articles.ArticlePage'),
        ),
        migrations.AlterField(
            model_name='articlepagerelatedpage',
            name='source_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_pages', to='articles.ArticlePage'),
        ),
    ]
