from django.contrib import admin
from django.contrib.auth import get_user_model

from fitnessEcommerceApp.accounts.models import AppProfile

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None,
         {'classes': ('wide',)},
         {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}
         )
    )

    search_fields = ('email',)

    ordering = ('email',)


@admin.register(AppProfile)
class AppProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'age', 'height', 'weight')
    search_fields = ('user__email', 'first_name', 'last_name')
    list_filter = ('age',)

    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name', 'age', 'height', 'weight', 'profile_picture')
        }),
    )

    readonly_fields = ('user',)
