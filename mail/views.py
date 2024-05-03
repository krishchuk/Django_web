from django.shortcuts import render
from django.views.generic import ListView

from mail.models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'mail/client_list.html'
    extra_context = {
        'title': "Список клиентов"
    }
