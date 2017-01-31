# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_ORDER_INFO',
            fields=[
                ('ORDER_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('ORDER_DATE', models.IntegerField(default=0)),
                ('ORDER_QTY', models.IntegerField(default=0)),
                ('ORDER_FIN', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'T_ORDER_INFO',
            },
        ),
        migrations.CreateModel(
            name='T_PROD_MACHINE',
            fields=[
                ('MACHINE_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('MACHINE_NAME', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'T_PROD_MACHINE',
            },
        ),
        migrations.CreateModel(
            name='T_PROD_PROCESS',
            fields=[
                ('PROCESS_ID', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('PROCESS_ORDER', models.IntegerField(default=0)),
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
                ('MACHINE_QTY', models.IntegerField(default=0)),
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
            ],
            options={
                'db_table': 'T_PROD_TYPE',
            },
        ),
        migrations.CreateModel(
            name='T_MACHINE_STATUS',
            fields=[
                ('MACHINE_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.T_PROD_MACHINE')),
                ('MACHINE_MTR', models.DateTimeField(null=True)),
                ('MACIHNE_LOAD', models.IntegerField(default=0)),
                ('MACHINE_LT', models.IntegerField(default=0)),
                ('MACHINE_CAPA', models.IntegerField(default=0)),
                ('MCAHINE_SCHED', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'T_MACHINE_STATUS',
            },
        ),
        migrations.AddField(
            model_name='t_prod_schedule',
            name='MACHINE_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_MACHINE'),
        ),
        migrations.AddField(
            model_name='t_prod_schedule',
            name='ORDER_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_ORDER_INFO'),
        ),
        migrations.AddField(
            model_name='t_prod_schedule',
            name='PROCESS_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_PROCESS'),
        ),
        migrations.AddField(
            model_name='t_prod_process',
            name='ITEM_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_TYPE'),
        ),
        migrations.AddField(
            model_name='t_order_info',
            name='ITEM_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.T_PROD_TYPE'),
        ),
    ]