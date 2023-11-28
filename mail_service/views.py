from random import random, sample
from smtplib import SMTPException

from Tools.demo.sortvisu import distinct
from apscheduler.schedulers.blocking import BlockingScheduler
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from client.models import Client
from config import settings
from mail_service.forms import MessagesForm
from mail_service.models import Messages, SettingsMailing, Logs
from post.models import Post


def home(request):

    random_post = Post.objects.filter(is_published='True').order_by('?')[:3]
    activ_mailing = Messages.objects.filter(is_active='True')

    message_count = Messages.objects.all()
    unique_clients = Client.objects.all().distinct()
    return render(request, 'mail_service/home.html', {'random_post': random_post, 'message_count': message_count, 'activ_mailing': activ_mailing,'unique_clients':unique_clients})

class MessagesCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    form_class = MessagesForm
    #fields = ('title', 'body', 'status', 'setting', 'clients')
    success_url = reverse_lazy('mail_service:list')
    permission_required = 'mailing_service.add_messages'

    def form_valid(self, form):
        message = form.save(commit=False)
        form.instance.user = self.request.user
        clients = ''
        message.save()
        if form.is_valid:
            clients = form.cleaned_data.get('clients')
            client_list = ",".join(str(x) for x in clients)
            client_email = client_list.split(',')
        for email in client_email:
            if message.status == 'К отправке' and message.setting.date_start <= message.date_create <= message.setting.date_stop:
                try:
                    send_mail(
                       subject=message.title,
                       message= message.body,
                       from_email=settings.EMAIL_HOST_USER,
                       recipient_list=[email],
                       fail_silently=False,
                       )
                    print(message.setting.date_start, message.date_create, message.setting.date_stop)
                    for client in clients:
                       Logs.objects.create(
                       message=message,
                       client=client,
                       status=Logs.STATUS_OK,
                       )

                except BadHeaderError as e:
                   print("Произошла ошибка BadHeaderError при отправке письма:", str(e))
                   Logs.objects.create(
                       message=message,
                       client=client,
                       status=Logs.STATUS_FAILED,
                       server_response="BadHeaderError: " + str(e),
                       )

                except SMTPException as e:
                   print("Произошла ошибка SMTP при отправке письма:", str(e))
                   Logs.objects.create(
                       message=message,
                       client=client,
                       status=Logs.STATUS_FAILED,
                       server_response="SMTPException: " + str(e),
                       )
        return super().form_valid(form)


class MessagesListView(ListView):
    model = Messages
    paginate_by = 3


class MessagesDetailView(DetailView):
    model = Messages
  #  slug_field = 'pk'
  #  slug_url_kwarg = 'pk'
   # template_name = 'mail_service:message_view'

class MessagesUpdateView(UpdateView):
    model = Messages
    fields = ('title', 'body')
   # slug_field = 'pk'
   # slug_url_kwarg = 'pk'
    success_url = reverse_lazy('mail_service:list')
   # def get_success_url(self):
   #     return reverse('messages:view',args=[self.kwargs.get('pk')])

class MessagesDeleteView(DeleteView):
    model = Messages
    success_url = reverse_lazy('mail_service:list')
   # slug_field = 'pk'
  #  slug_url_kwarg = 'pk'



class LogsListView(ListView):
    model = Logs
    logs_list = Logs.objects.all()#.count()
    template_name = 'mail_service/logs_list.html'
    paginate_by = 10