from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'function',)
    raw_id_fields = ['user']
    search_fields = ('user__username', 'company',)

admin.site.register(UserProfile, UserProfileAdmin)
