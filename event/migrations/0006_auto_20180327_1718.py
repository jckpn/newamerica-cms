# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-27 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_related_conference'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alleventshomepage',
            options={'verbose_name': 'Events Homepage'},
        ),
        migrations.AlterModelOptions(
            name='programeventspage',
            options={'verbose_name': 'Events Homepage'},
        ),
    ]
