# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-24 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='generate_pdf_on_publish',
            field=models.BooleanField(default=False, help_text=b'If checked, the download button on reports will link to the generated pdf. Otherwise, upload a pdf to the "Report PDF" field'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_pdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name=b'Report PDF'),
        ),
    ]