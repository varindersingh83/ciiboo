# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 06:19
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20170609_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='my_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AUT', 'Delivery'), ('DEU', 'Take-Away')], default=0, max_length=7),
        ),
    ]