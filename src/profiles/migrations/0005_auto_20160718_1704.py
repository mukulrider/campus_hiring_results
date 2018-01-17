# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_mainprofile_personalis_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainprofile',
            old_name='overall_highest',
            new_name='aptus_percentile',
        ),
        migrations.RenameField(
            model_name='mainprofile',
            old_name='overall_avg',
            new_name='latus_percentile',
        ),
        migrations.RenameField(
            model_name='mainprofile',
            old_name='overall_cand',
            new_name='overall_percentile',
        ),
        migrations.RenameField(
            model_name='mainprofile',
            old_name='total_questions',
            new_name='tekhne_percentile',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='correctly_answered',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='incorrectly_answered',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='personalis_avg',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='personalis_cand',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='personalis_highest',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='tekne_avg',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='tekne_cand',
        ),
        migrations.RemoveField(
            model_name='mainprofile',
            name='tekne_highest',
        ),
        migrations.AddField(
            model_name='mainprofile',
            name='tekhne_avg',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Tekhne avg'),
        ),
        migrations.AddField(
            model_name='mainprofile',
            name='tekhne_cand',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Tekhne score'),
        ),
        migrations.AddField(
            model_name='mainprofile',
            name='tekhne_highest',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Tekhne highest'),
        ),
    ]