# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('person', '0016_auto_20160404_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardAndLeadershipPeoplePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_description', wagtail.wagtailcore.fields.RichTextField(blank=True, null=True)),
                ('role_query', models.CharField(choices=[(b'Board Member', b'Board Members'), (b'Leadership Team', b'Leadership Team'), (b'Central Staff', b'Central Staff')], default=b'Board Members', max_length=50)),
            ],
            options={
                'verbose_name': 'Our People Page for Board of Directors, Central Staff, and Leadership Team',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='ourpeoplepage',
            options={'verbose_name': 'Homepage for All People in NAF'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='location',
        ),
    ]