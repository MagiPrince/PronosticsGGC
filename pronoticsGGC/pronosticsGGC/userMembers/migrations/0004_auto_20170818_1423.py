# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userMembers', '0003_remove_profil_nbcoins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profil',
            name='nbGGCPoints',
            field=models.IntegerField(default=0),
        ),
    ]
