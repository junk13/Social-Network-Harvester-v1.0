# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-28 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ytcomment',
            name='text_truncated',
            field=models.BooleanField(default=False),
        ),
    ]