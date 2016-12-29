# -*- coding: UTF-8 -*-
from django.db import models
import datetime


# Create your models here.
class SAPAccountAudit(models.Model):
    inputdate = models.DateField('导入日期',default=datetime.datetime.now)
    usercode = models.CharField('用户编号',max_length=20)
    sid = models.CharField('系统编号',max_length=3)
    type = models.CharField('类型',max_length=10)
    creator = models.CharField('创建者',max_length=20)
    create_on = models.DateField('创建时间',default=datetime.date(1970,01,01))
    valid_from = models.DateField('有效自',default=datetime.date(1970,01,01))
    Last_logon_d = models.DateField('最后登录日期',default=datetime.date(1970,01,01))
    Last_logon_t = models.TimeField('最后登录时间',default=datetime.time(00,00,00))
    def __unicode__(self):
        return self.name

class ODM(models.Model):
    ORG_CODE = models.CharField('组织代码',max_length=32)  
    ORG_NAME = models.CharField('组织名称',max_length=32)
    CORP_CODE = models.CharField('公司代码',max_length=32)
    CORP_NAME = models.CharField('公司名称',max_length=32)
    DEPT_CODE = models.CharField('部门代码',max_length=50)
    DEPT_NAME = models.CharField('部门名称',max_length=50)
    USER_CODE = models.CharField('用户编号',max_length=20)
    USER_NAME = models.CharField('用户名称',max_length=20)
    USER_EMAIL = models.CharField('邮箱地址',max_length=128)
    USER_SEX = models.CharField('性别',max_length=32)
    USER_TYPE = models.CharField('用户类别',max_length=32)
    CREATE_TIME = models.DateTimeField('创建时间',default=datetime.datetime(1970,01,01,00,00,00))
    LAST_UPDATE_USER_NAME = models.CharField('最后修改者',max_length=32)
    LAST_UPDATE_TIME = models.DateTimeField('最后修改时间',default=datetime.datetime(1970,01,01,00,00,00))
    def __unicode__(self):
        return self.name