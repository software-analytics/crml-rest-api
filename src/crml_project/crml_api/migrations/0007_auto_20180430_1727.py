# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crml_api', '0006_auto_20180430_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
