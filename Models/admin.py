from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


admin.site.register(models.Account, UserAdmin)
admin.site.register(models.Announcements)
admin.site.register(models.Events)
admin.site.register(models.Messages)


