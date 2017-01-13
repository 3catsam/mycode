# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ODM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ORG_CODE', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe4\xbb\xa3\xe7\xa0\x81')),
                ('ORG_NAME', models.CharField(max_length=32, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('CORP_CODE', models.CharField(max_length=32, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\xa3\xe7\xa0\x81')),
                ('CORP_NAME', models.CharField(max_length=32, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('DEPT_CODE', models.CharField(max_length=50, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe4\xbb\xa3\xe7\xa0\x81')),
                ('DEPT_NAME', models.CharField(max_length=50, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('USER_CODE', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xbc\x96\xe5\x8f\xb7')),
                ('USER_NAME', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('USER_EMAIL', models.CharField(max_length=128, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\x9c\xb0\xe5\x9d\x80')),
                ('USER_SEX', models.CharField(max_length=32, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('USER_TYPE', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x88\xab')),
                ('CREATE_TIME', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('LAST_UPDATE_USER_NAME', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe8\x80\x85')),
                ('LAST_UPDATE_TIME', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='SAPAccountAudit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inputdate', models.DateField(default=datetime.datetime.now, verbose_name=b'\xe5\xaf\xbc\xe5\x85\xa5\xe6\x97\xa5\xe6\x9c\x9f')),
                ('usercode', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xbc\x96\xe5\x8f\xb7')),
                ('sid', models.CharField(max_length=3, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xbc\x96\xe5\x8f\xb7')),
                ('type', models.CharField(max_length=10, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('creator', models.CharField(max_length=20, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85')),
                ('create_on', models.DateField(default=datetime.date(1970, 1, 1), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('valid_from', models.DateField(default=datetime.date(1970, 1, 1), verbose_name=b'\xe6\x9c\x89\xe6\x95\x88\xe8\x87\xaa')),
                ('Last_logon_d', models.DateField(default=datetime.date(1970, 1, 1), verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe7\x99\xbb\xe5\xbd\x95\xe6\x97\xa5\xe6\x9c\x9f')),
                ('Last_logon_t', models.TimeField(default=datetime.time(0, 0), verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe7\x99\xbb\xe5\xbd\x95\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
