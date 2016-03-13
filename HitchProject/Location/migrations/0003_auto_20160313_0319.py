# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0002_auto_20160313_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='StateProv',
        ),
        migrations.RemoveField(
            model_name='location',
            name='addr',
        ),
        migrations.RemoveField(
            model_name='location',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longi',
        ),
        migrations.RemoveField(
            model_name='location',
            name='zipCode',
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='test', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='place_id',
            field=models.CharField(default='null', max_length=60),
            preserve_default=False,
        ),
    ]
