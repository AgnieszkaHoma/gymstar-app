from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomModelUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(User, CustomModelUserAdmin)
class CustomModelUserProfileAdmin(UserAdmin):
    list_display = ('name', 'surname', 'email')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(UserProfile, CustomModelUserProfileAdmin)
