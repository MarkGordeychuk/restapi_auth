from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('login', 'is_staff', 'is_active',)
    list_filter = ('login', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('login', 'phone', 'name', 'birth', 'password')}),
        (_("Personal info"), {"fields": ("tg", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
             'classes': ('wide',),
             'fields': ('login', 'phone', 'name', 'birth', 'password1', 'password2', 'is_staff', 'is_active',),
        },
        ),
    )
    search_fields = ('login',)
    ordering = ('login',)


admin.site.register(User, UserAdmin)
