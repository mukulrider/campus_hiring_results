# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160718_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainprofile',
            name='aptus_percentile',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Aptus Percentile'),
        ),
        migrations.AlterField(
            model_name='mainprofile',
            name='latus_percentile',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Latus Percentile'),
        ),
        migrations.AlterField(
            model_name='mainprofile',
            name='overall_percentile',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Overall Percentile'),
        ),
        migrations.AlterField(
            model_name='mainprofile',
            name='tekhne_percentile',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Tekhne Percentile'),
        ),
    ]
