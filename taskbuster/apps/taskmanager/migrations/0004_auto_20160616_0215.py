# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20160615_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the task name', max_length=100, verbose_name='name')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='taskmanager.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'Task',
                'ordering': ('project', 'name'),
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set([('project', 'name')]),
        ),
    ]
