# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-14 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
