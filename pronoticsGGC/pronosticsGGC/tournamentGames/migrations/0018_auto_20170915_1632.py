# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 14:32
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tournamentGames', '0017_auto_20170915_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchopponents',
            old_name='equipe',
            new_name='equipeTwo',
        ),
        migrations.AddField(
            model_name='matchopponents',
            name='equipeOne',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='gameName', chained_model_field='teamGame', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='equipeOne', to='tournamentGames.TeamGGC'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='winner',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='matchNumber', chained_model_field='equipeOne', on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='tournamentGames.TeamGGC'),
        ),
    ]