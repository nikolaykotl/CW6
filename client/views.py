from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from client.models import Client

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('first_name','last_name', 'email')
    success_url = reverse_lazy('client:list')
    permission_required = 'mailing_service.add_client'

class ClientListView(ListView):
    model = Client
    client_list = Client.objects.all().distinct()


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    fields = ('first_name','last_name', 'email')
    permission_required = 'mailing_service.change_client'

    def get_success_url(self):
        return reverse('client:view',args=[self.kwargs.get('pk')])

class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')
    permission_required = 'mailing_service.delete_client'
