from django.contrib import admin
from django.contrib.auth.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff']
    list_editable = ['is_staff']
    search_fields = ['username', 'email']
    
