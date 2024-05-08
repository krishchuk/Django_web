from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Blog
from mail.forms import ClientForms, EmailSettingsForms, EmailMessageForms
from mail.models import Client, EmailSettings, EmailMessage, EmailTry
from mail.services import get_all_mailings_count_from_cache, get_active_mailings_count_from_cache, \
    get_clients_count_from_cache


class HomeView(TemplateView):
    template_name = 'mail/home.html'
    extra_context = {
            'title': 'Mail - Сервис Ваших рассылок'
        }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data()
        blog_list = Blog.objects.order_by('?')[:3]

        context_data['all_mailings_count'] = get_all_mailings_count_from_cache()
        context_data['active_mailings_count'] = get_active_mailings_count_from_cache()
        context_data['unique_clients_count'] = get_clients_count_from_cache()
        context_data['blog_list'] = blog_list

        return context_data


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': "Список клиентов"
    }


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    extra_context = {
        'title': "Описание клиента"
    }


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('mail:client_list')
    extra_context = {
        'title': "Добавить клиента"
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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
    success_url = reverse_lazy('mail:settings_list')
    extra_context = {
        'title': "Добавить настройку рассылки"
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EmailSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailSettings
    form_class = EmailSettingsForms
    success_url = reverse_lazy('mail:settings_list')
    extra_context = {
        'title': "Настроить рассылку"
    }


class EmailSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = EmailSettings
    success_url = reverse_lazy('mail:settings_list')
    extra_context = {
        'title': "Удалить настройку рассылки"
    }


class EmailSettingsListView(LoginRequiredMixin, ListView):
    model = EmailSettings
    extra_context = {
        'title': "Список рассылок"
    }


class EmailMessageCreateView(LoginRequiredMixin, CreateView):
    model = EmailMessage
    form_class = EmailMessageForms()
    success_url = reverse_lazy('mail:mail_list')
    extra_context = {
        'title': "Создать письмо"
    }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EmailMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailMessage
    form_class = EmailMessageForms
    success_url = reverse_lazy('mail:mail_list')
    extra_context = {
        'title': "Изменить письмо"
    }


class EmailMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = EmailMessage
    success_url = reverse_lazy('mail:mail_list')
    extra_context = {
        'title': "Удалить письмо"
    }


class EmailMessageListView(LoginRequiredMixin, ListView):
    model = EmailMessage
    extra_context = {
        'title': "Список писем"
    }


class EmailTryListView(LoginRequiredMixin, ListView):
    model = EmailTry
    extra_context = {
        'title': "Отчет проведенных рассылок"
    }
