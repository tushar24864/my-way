from django.contrib import admin
from app.models import confidential
# Register your models here.
class Admin_Confidential(admin.ModelAdmin):
    list_display=("employee","img","datetime")

admin.site.register(confidential,Admin_Confidential)