# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
