# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0005_rename_flowcls'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
