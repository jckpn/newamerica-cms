# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-17 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_populate_post_ordered_date_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ordered_date_string',
            field=models.CharField(blank=True, default='', max_length=140),
            preserve_default=False,
        ),
    ]
