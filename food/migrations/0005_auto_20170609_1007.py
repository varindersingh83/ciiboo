# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_remove_blog_first_aid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='openingstatus',
            field=models.CharField(choices=[('Open', 'Open'), ('Opening Soon', 'Opening Soon')], max_length=60, unique=True),
        ),
    ]