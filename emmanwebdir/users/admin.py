from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'last_login')}),
        ('Permissions', {'fields': (
            'is_allow',
            'is_active', 
            'is_staff', 
            'is_superuser',
            'is_teacher',
            'is_student',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2','is_staff', 'is_superuser', 'is_active','is_teacher','is_student','is_allow', 'groups',)
            }
        ),
    )

    list_display = ('email', 'username', 'is_staff', 'last_login','is_teacher','is_student','is_allow',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)