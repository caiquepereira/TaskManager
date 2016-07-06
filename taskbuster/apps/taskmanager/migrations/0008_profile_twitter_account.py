# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0007_project_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='twitter_account',
            field=models.CharField(default=b'', help_text='Enter your twitter account', max_length=100, verbose_name='twitter_account'),
        ),
    ]
