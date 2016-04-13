# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0017_auto_20160411_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardandleadershippeoplepage',
            options={'verbose_name': 'Our People Page for Board of Directors, Central Staff, and Leadership Team'},
        ),
        migrations.AlterModelOptions(
            name='ourpeoplepage',
            options={'verbose_name': 'Homepage for All People in NAF'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='location',
        ),
        migrations.AlterField(
            model_name='boardandleadershippeoplepage',
            name='role_query',
            field=models.CharField(choices=[(b'Board Member', b'Board Members'), (b'Leadership Team', b'Leadership Team'), (b'Central Staff', b'Central Staff')], default=b'Board Members', max_length=50),
        ),
    ]
