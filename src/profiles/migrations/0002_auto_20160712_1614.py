# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email_verified',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
