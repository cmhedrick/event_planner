# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 20:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_planner_app', '0002_auto_20170810_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
    ]
