# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TeamGGC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=100)),
                ('stillInCompetition', models.BooleanField(default=True)),
                ('teamGame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournamentGames.GameName')),
            ],
        ),
    ]
