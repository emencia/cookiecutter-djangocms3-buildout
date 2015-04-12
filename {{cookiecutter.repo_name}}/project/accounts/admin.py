from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'function',)
    raw_id_fields = ['user']
    search_fields = ('user__username', 'company',)

admin.site.register(UserInfo, UserInfoAdmin)
