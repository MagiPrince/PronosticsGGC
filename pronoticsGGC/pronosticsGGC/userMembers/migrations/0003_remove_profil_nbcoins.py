# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userMembers', '0002_auto_20170802_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='nbCoins',
        ),
    ]
