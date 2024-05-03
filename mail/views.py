from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from mail.forms import ClientForms, EmailSettingsForms, EmailMessageForms
from mail.models import Client, EmailSettings, EmailMessage


class HomeView(TemplateView):
    template_name = 'mail/home.html'
    extra_context = {
            'title': "Mail - Сервис Ваших рассылок"
        }


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': "Список клиентов"
    }


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    extra_context = {
        'title': "Описание клиента"
    }

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['client'] = self.object
    #     return context_data


# def client_detail(request, pk):
#     """Отображение деталей клиента."""
#     client = Client.objects.get(pk=pk)
#     return render(request, 'spam_mail/client_detail.html', {'client': client})


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('mail:client_list')
    extra_context = {
        'title': "Добавить клиента"
    }


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('mail:client_list')
    extra_context = {
        'title': "Изменить данные клиента"
    }


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:client_list')
    extra_context = {
        'title': "Удалить клиента"
    }


class EmailSettingsCreateView(LoginRequiredMixin, CreateView):
    model = EmailSettings
    form_class = EmailSettingsForms
    success_url = reverse_lazy('mail:home')
    extra_context = {
        'title': "Добавить настройку рассылки"
    }


class EmailSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailSettings
    form_class = EmailSettingsForms
    success_url = reverse_lazy('mail:home')
    extra_context = {
        'title': "Настроить рассылку"
    }


class EmailSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = EmailSettings
    success_url = reverse_lazy('mail:home')
    extra_context = {
        'title': "Удалить настройку рассылки"
    }


class EmailSettingsListView(ListView):
    model = EmailSettings
    extra_context = {
        'title': "Список рассылок"
    }


class EmailMessageCreateView(LoginRequiredMixin, CreateView):
    model = EmailMessage
    form_class = EmailMessageForms
    success_url = reverse_lazy('mail:home')
    extra_context = {
        'title': "Создать письмо"
    }


class EmailMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailMessage
    form_class = EmailMessageForms
    success_url = reverse_lazy('mail:home')
    extra_context = {
        'title': "Изменить письмо"
    }


class EmailMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = EmailMessage
    success_url = reverse_lazy('mail:home')
    extra_context = {
        'title': "Удалить письмо"
    }


class EmailMessageListView(ListView):
    model = EmailMessage
    extra_context = {
        'title': "Список писем"
    }
