# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")),
            ],
        ),
    ]
