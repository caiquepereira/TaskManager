# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0006_auto_20160706_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
