# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kik', '0006_request_document_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='document_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]