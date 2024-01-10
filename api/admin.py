from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'is_active', 'is_staff', 'created_at', 'updated_at']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('created_at', 'updated_at')}),
    )

admin.site.register(User, CustomUserAdmin)
