# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_auto_20160627_0025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='candidate_muapt_scores',
            new_name='muapt_scores',
        ),
    ]
