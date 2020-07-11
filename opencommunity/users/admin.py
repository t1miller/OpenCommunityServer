from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserCreationForm
    list_display = ['email', 'username', 'name']


admin.site.register(CustomUser, CustomUserAdmin)
