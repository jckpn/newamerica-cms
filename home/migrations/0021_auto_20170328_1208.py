# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-28 16:08
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20170221_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgsimplepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial')), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'schedule', wagtail.wagtailcore.blocks.StreamBlock([(b'days', wagtail.wagtailcore.blocks.StructBlock([(b'collapsible', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'Allow schedule sessions to expand and collapse', required=False)), (b'day', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')], default=1, help_text=b'What day of the conference is this session on?', required=False)), (b'start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'sessions', wagtail.wagtailcore.blocks.StreamBlock([(b'session', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock()), (b'session_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'panel', b'Panel'), (b'lecture', b'Lecture'), (b'break', b'Break'), (b'meal', b'Meal'), (b'reception', b'Reception'), (b'registration', b'Registration')])), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'speakers', wagtail.wagtailcore.blocks.StreamBlock([(b'speaker', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.TextBlock(required=False))]))])), (b'archived_video_link', wagtail.wagtailcore.blocks.URLBlock(help_text=b'Enter youtube link after conference', required=False))]))]))]))], help_text=b'1 to 2 day schedule of events', icon=b'date')), (b'people', wagtail.wagtailcore.blocks.StreamBlock([(b'person', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.TextBlock(help_text=b'125 character limit', max_length=125, required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'twitter', wagtail.wagtailcore.blocks.URLBlock(required=False))]))], help_text=b'Grid of people with short bios that appear on click', icon=b'group')), (b'panels', wagtail.wagtailcore.blocks.StreamBlock([(b'panel', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.TextBlock()), (b'body', wagtail.wagtailcore.blocks.StreamBlock([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial')), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site'))]))], icon=b'doc-empty-inverse'))], icon=b'list-ul')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Legacy option. Consider using Inline Image instead.', icon=b'placeholder', template=b'blocks/image_block.html'))]),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial')), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'schedule', wagtail.wagtailcore.blocks.StreamBlock([(b'days', wagtail.wagtailcore.blocks.StructBlock([(b'collapsible', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'Allow schedule sessions to expand and collapse', required=False)), (b'day', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')], default=1, help_text=b'What day of the conference is this session on?', required=False)), (b'start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'sessions', wagtail.wagtailcore.blocks.StreamBlock([(b'session', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock()), (b'session_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'panel', b'Panel'), (b'lecture', b'Lecture'), (b'break', b'Break'), (b'meal', b'Meal'), (b'reception', b'Reception'), (b'registration', b'Registration')])), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'speakers', wagtail.wagtailcore.blocks.StreamBlock([(b'speaker', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.TextBlock(required=False))]))])), (b'archived_video_link', wagtail.wagtailcore.blocks.URLBlock(help_text=b'Enter youtube link after conference', required=False))]))]))]))], help_text=b'1 to 2 day schedule of events', icon=b'date')), (b'people', wagtail.wagtailcore.blocks.StreamBlock([(b'person', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.TextBlock(help_text=b'125 character limit', max_length=125, required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'twitter', wagtail.wagtailcore.blocks.URLBlock(required=False))]))], help_text=b'Grid of people with short bios that appear on click', icon=b'group')), (b'panels', wagtail.wagtailcore.blocks.StreamBlock([(b'panel', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.TextBlock()), (b'body', wagtail.wagtailcore.blocks.StreamBlock([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial')), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site'))]))], icon=b'doc-empty-inverse'))], icon=b'list-ul')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Legacy option. Consider using Inline Image instead.', icon=b'placeholder', template=b'blocks/image_block.html'))]),
        ),
        migrations.AlterField(
            model_name='programsimplepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial')), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'schedule', wagtail.wagtailcore.blocks.StreamBlock([(b'days', wagtail.wagtailcore.blocks.StructBlock([(b'collapsible', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'Allow schedule sessions to expand and collapse', required=False)), (b'day', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')], default=1, help_text=b'What day of the conference is this session on?', required=False)), (b'start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'sessions', wagtail.wagtailcore.blocks.StreamBlock([(b'session', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock()), (b'session_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'panel', b'Panel'), (b'lecture', b'Lecture'), (b'break', b'Break'), (b'meal', b'Meal'), (b'reception', b'Reception'), (b'registration', b'Registration')])), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), (b'speakers', wagtail.wagtailcore.blocks.StreamBlock([(b'speaker', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.TextBlock(required=False))]))])), (b'archived_video_link', wagtail.wagtailcore.blocks.URLBlock(help_text=b'Enter youtube link after conference', required=False))]))]))]))], help_text=b'1 to 2 day schedule of events', icon=b'date')), (b'people', wagtail.wagtailcore.blocks.StreamBlock([(b'person', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.TextBlock(help_text=b'125 character limit', max_length=125, required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'twitter', wagtail.wagtailcore.blocks.URLBlock(required=False))]))], help_text=b'Grid of people with short bios that appear on click', icon=b'group')), (b'panels', wagtail.wagtailcore.blocks.StreamBlock([(b'panel', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.TextBlock()), (b'body', wagtail.wagtailcore.blocks.StreamBlock([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial')), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site'))]))], icon=b'doc-empty-inverse'))], icon=b'list-ul')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Legacy option. Consider using Inline Image instead.', icon=b'placeholder', template=b'blocks/image_block.html'))]),
        ),
    ]
