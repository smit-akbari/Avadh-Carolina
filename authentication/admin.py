from django.contrib import admin
from .models import membersModel, memberProfileModel
# Register your models here.

admin.site.register(membersModel)
admin.site.register(memberProfileModel)