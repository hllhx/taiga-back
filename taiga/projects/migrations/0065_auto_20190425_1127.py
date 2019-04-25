# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-25 11:27
from __future__ import unicode_literals

import django.core.serializers.json
from django.db import migrations
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0064_auto_20190408_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='discard',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='notnow',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]
