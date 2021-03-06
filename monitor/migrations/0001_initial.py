# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=64)),
                ('height', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForkState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_forked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('best_block_hash', models.CharField(max_length=64)),
                ('best_block_height', models.IntegerField()),
                ('prev_block_hash', models.CharField(max_length=64)),
                ('has_reorged', models.BooleanField(default=False)),
                ('is_behind', models.BooleanField(default=False)),
                ('highest_divergence', models.IntegerField(default=0)),
                ('highest_diverged_hash', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Node'),
        ),
        migrations.AddField(
            model_name='block',
            name='prev',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitor.Block'),
        ),
    ]
