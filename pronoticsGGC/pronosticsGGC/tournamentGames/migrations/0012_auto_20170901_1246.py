# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournamentGames', '0011_matchresult_maj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prognostic',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournamentGames.MatchOpponents'),
        ),
    ]
