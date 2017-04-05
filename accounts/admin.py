from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'school']


admin.site.register(User, MyUserAdmin)
