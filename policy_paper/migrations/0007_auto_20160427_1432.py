# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-27 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policy_paper', '0006_auto_20160404_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policypaper',
            name='publication_cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.CustomImage'),
        ),
    ]