from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):
    list_display = ('username', 'email', 'birthday')
    list_display_links = ('username',)
    search_fields = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("birthday",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("birthday",)}),)


