from django.contrib import admin

# Register your models here.
from sap.models import ODM,SAPAccountAudit

admin.site.register(ODM)
admin.site.register(SAPAccountAudit)
