# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='available',
            field=models.CharField(max_length=300),
        ),
    ]
