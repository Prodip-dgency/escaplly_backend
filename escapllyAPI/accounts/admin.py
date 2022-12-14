from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, UserProfile


class CustomUserAdmin(UserAdmin):

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )

admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(UserProfile)