# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 08:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startUpGoggleApp', '0003_auto_20170806_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publish', models.DateTimeField(default=datetime.datetime.now)),
                ('isActive', models.BooleanField(default='False')),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
