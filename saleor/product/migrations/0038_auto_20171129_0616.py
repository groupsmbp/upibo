# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 12:16
from __future__ import unicode_literals

from django.contrib.postgres.operations import BtreeGinExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20171124_0847'),
    ]

    operations = [
        BtreeGinExtension()
    ]
