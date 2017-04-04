from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'password', 'username', 'school', 'groups')
    list_display = ['first_name', 'last_name',  'username', 'school']

admin.site.register(User, UserAdmin)
