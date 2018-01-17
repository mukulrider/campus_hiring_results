# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160712_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainprofile',
            name='overall_avg',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Overall avg'),
        ),
        migrations.AddField(
            model_name='mainprofile',
            name='overall_cand',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Overall score'),
        ),
        migrations.AddField(
            model_name='mainprofile',
            name='overall_highest',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Overall highest'),
        ),
    ]
