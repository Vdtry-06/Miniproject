from django.contrib import admin

from django.contrib.auth.models import Group
# Register your models here.
admin.site.unregister(Group)

from .models import *
# admin.site.register(Customer)
admin.site.register(Video)
admin.site.register(UserStatus)
