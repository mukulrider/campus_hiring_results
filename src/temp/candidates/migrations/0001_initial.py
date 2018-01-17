# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('password', models.TextField(blank=True, max_length=500, verbose_name='Desc')),
            ],
        ),
    ]
