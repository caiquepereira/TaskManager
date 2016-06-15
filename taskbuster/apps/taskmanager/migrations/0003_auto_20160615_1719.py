# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20160615_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'ordering': ('user', 'name'),
                'verbose_name': 'Tag',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('user', 'name')]),
        ),
    ]