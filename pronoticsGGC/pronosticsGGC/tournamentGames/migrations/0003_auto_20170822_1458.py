# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournamentGames', '0002_matchopponents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchopponents',
            name='matchStarting',
            field=models.DateTimeField(),
        ),
    ]
