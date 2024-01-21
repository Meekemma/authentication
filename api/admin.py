from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'username', 'is_active', 'is_staff', 'created_at', 'updated_at', 'role', 'last_role_switch_date']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at', 'last_role_switch_date')}),
        ('User Role', {'fields': ('role',)}),
    )

    # Exclude 'first_name' and 'last_name' from the form
    exclude = ('first_name', 'last_name')

    readonly_fields = ('last_role_switch_date',)

admin.site.register(User, CustomUserAdmin)
