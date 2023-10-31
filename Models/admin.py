from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Account)
admin.site.register(models.Announcements)
admin.site.register(models.Events)
admin.site.register(models.Messages)


