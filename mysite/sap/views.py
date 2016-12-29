# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sap.models import ODM,SAPAccountAudit


def content(request):
    content_odmall = ODM.objects.all()
    content_odm  = map(str, content_odmall)
    return HttpResponse(content_odmall)

def first_page(request):
    return HttpResponse("<p>SAP</p>")