from django.contrib import admin

# Register your models here.
from .models import Profile,Skill,Message,Announcement,Notes

# admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
admin.site.register(Announcement)
admin.site.register(Notes)