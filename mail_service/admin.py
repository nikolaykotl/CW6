from django.contrib import admin

from mail_service.models import Messages, SettingsMailing
from users.models import User


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'setting', 'is_active')
    list_filter = ('setting', 'clients', 'is_active')
    search_fields = ('title', 'body', 'setting',)
    filter_horizontal = ['clients']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_superuser:
            return form

        elif request.user.is_staff:
            form.base_fields['title'].disabled = True
            form.base_fields['body'].disabled = True
            form.base_fields['setting'].disabled = True
            form.base_fields['clients'].disabled = True
            form.base_fields['user'].disabled = True
            form.base_fields['status'].disabled = True
            return form

@admin.register(SettingsMailing)
class SettingsMailingAdmin(admin.ModelAdmin):

    list_display = ('id', 'regularity',)
    list_filter = ('regularity',)
    search_fields = ('regularity',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'avatar', 'country', 'is_block')
    list_filter = ('country', 'is_block')
   # search_fields = ('title', 'body', 'setting',)
   # filter_horizontal = ['clients']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_superuser:
            return form

        elif request.user.is_staff:
            form.base_fields['email'].disabled = True
            form.base_fields['phone'].disabled = True
            form.base_fields['avatar'].disabled = True
            form.base_fields['country'].disabled = True
            form.base_fields['email_verify'].disabled = True

            return form

