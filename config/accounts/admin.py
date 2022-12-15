from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'phone_no', 'type_utilisateur' ] # new
    # fieldsets = UserAdmin.fieldsets + ( # new
    # (None, {'fields': ('email', 'first_name', 'last_name', 'phone_no', 'type_utilisateur')}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + ( # new
    # (None, {'fields': ('email', 'phone_no', 'first_name', 'last_name', 'phone_no', 'type_utilisateur')}),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
