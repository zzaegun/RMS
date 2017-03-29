# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_MACHINE_STATUS',
            fields=[
                ('MACHINE_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('MACHINE_MTR', models.DateTimeField(null=True)),
                ('MACHINE_LOAD', models.IntegerField(default=0)),
                ('MACHINE_LT', models.IntegerField(default=0)),
                ('MACHINE_CAPA', models.IntegerField(default=0)),
                ('MACHINE_NAME', models.CharField(max_length=10)),
                ('MACHINE_SCHED', models.DateTimeField(null=True)),
                ('MACHINE_ENABLED', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'T_MACHINE_STATUS',
            },
        ),
        migrations.CreateModel(
            name='T_ORDER_INFO',
            fields=[
                ('ORDER_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('ORDER_DATE', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORDER_QTY', models.IntegerField(default=0)),
                ('ORDER_FIN', models.BooleanField(default=False)),
                ('FIN_TIME', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'T_ORDER_INFO',
            },
        ),
        migrations.CreateModel(
            name='T_PROD_PROCESS',
            fields=[
                ('PROCESS_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('SUBPROC_ORDER', models.TextField()),
                ('PROCESS_NAME', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'T_PROD_PROCESS',
            },
        ),
        migrations.CreateModel(
            name='T_PROD_SCHEDULE',
            fields=[
                ('SCHEDULE_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('UPDATE_TIME', models.DateTimeField(auto_now_add=True, null=True)),
                ('PROD_SCHED', models.DateTimeField(null=True)),
                ('MACHINE_USE', models.TextField()),
                ('MACHINE_QTY', models.IntegerField(default=0)),
                ('ORDER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_ORDER_INFO')),
                ('PROCESS_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_PROCESS')),
            ],
            options={
                'db_table': 'T_PROD_SCHEDULE',
            },
        ),
        migrations.CreateModel(
            name='T_PROD_TYPE',
            fields=[
                ('ITEM_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('ITEM_NAME', models.CharField(max_length=10)),
                ('PROCESS_ID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_PROCESS')),
            ],
            options={
                'db_table': 'T_PROD_TYPE',
            },
        ),
        migrations.CreateModel(
            name='T_SUB_PROCESS',
            fields=[
                ('SUBPROC_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('SUBPROC_NAME', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'T_SUB_PROCESS',
            },
        ),
        migrations.AddField(
            model_name='t_order_info',
            name='ITEM_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_TYPE'),
        ),
        migrations.AddField(
            model_name='t_machine_status',
            name='SUBPROC_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.T_SUB_PROCESS'),
        ),
    ]
