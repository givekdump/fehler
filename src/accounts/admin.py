from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Invite


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Invite)