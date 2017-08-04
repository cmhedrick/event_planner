# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 01:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event_planner_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('company', models.CharField(max_length=35)),
                ('phone_number', models.CharField(max_length=10)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='load_in',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 1, 30, 27, 832311, tzinfo=utc), verbose_name='Load In'),
        ),
        migrations.AddField(
            model_name='event',
            name='load_out',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 1, 30, 27, 832331, tzinfo=utc), verbose_name='Load Out'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 1, 30, 27, 831741, tzinfo=utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 1, 30, 27, 832290, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 1, 30, 27, 832262, tzinfo=utc), verbose_name='Start Date'),
        ),
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='event_planner_app.Client'),
            preserve_default=False,
        ),
    ]