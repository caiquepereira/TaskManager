# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_task_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
    ]
