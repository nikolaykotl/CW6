from django.urls import path
from django.views.decorators.cache import cache_page

from mail_service.apps import MailServiceConfig
from mail_service.views import MessagesListView, MessagesCreateView, MessagesDetailView, MessagesUpdateView, \
    MessagesDeleteView, LogsListView, home

app_name = MailServiceConfig.name


urlpatterns = [
    path('', cache_page(60)(home), name='home'),
    path('create/',MessagesCreateView.as_view(), name='create'),
    path('list/',MessagesListView.as_view(), name='list'),
    path('view/<int:pk>', MessagesDetailView.as_view(), name='message_view'),
    path('edit/<int:pk>', MessagesUpdateView.as_view(), name='message_edit'),
    path('delete/<int:pk>', MessagesDeleteView.as_view(), name='message_delete'),
    path('logs/', LogsListView.as_view(), name='logs')


    ]
