# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tournamentGames', '0009_auto_20170830_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchresult',
            name='test',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
