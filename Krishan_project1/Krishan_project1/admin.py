from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from .models import *



class Krishna_ProjectAdmin(admin.ModelAdmin):
        list_display = ("Name", "Email_ID", "country_name", "phone_no", "message")
admin.site.register(Krishna_Project, Krishna_ProjectAdmin)

