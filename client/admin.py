from django.contrib import admin

from client.models import Client
from mail_service.models import Messages


class ClientAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'last_name', 'first_name', 'patronymic', 'comment',)
    list_filter = ('email', 'last_name')
    search_fields = ('email',)
   # filter_horizontal = ['message']
   ## def _message(self, row):
   #     object = Messages.objects.all()
   #     ids = []
   #     for message in object:
   #         ids.append(message.id)
   #     return ids

admin.site.register(Client, ClientAdmin)