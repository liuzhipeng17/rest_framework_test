# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 10:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderby', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='views',
            old_name='vistor',
            new_name='tor',
        ),
    ]
