from django.urls import path
from django.views.decorators.cache import cache_page

from mail.apps import MailConfig
from mail.views import ClientListView, ClientDeleteView, ClientCreateView, ClientUpdateView, ClientDetailView, \
    EmailSettingsListView, EmailSettingsCreateView, EmailSettingsUpdateView, EmailSettingsDeleteView, \
    EmailMessageListView, EmailMessageCreateView, EmailMessageUpdateView, EmailMessageDeleteView, HomeView

app_name = MailConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>', cache_page(60)(ClientDetailView.as_view()), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    #
    path('email_settings/', EmailSettingsListView.as_view(), name='settings_list'),
    path('email_settings/create/', EmailSettingsCreateView.as_view(), name='settings_create'),
    path('email_settings/<int:pk>/update/', EmailSettingsUpdateView.as_view(), name='settings_update'),
    path('email_settings/<int:pk>/delete/', EmailSettingsDeleteView.as_view(), name='settings_delete'),
    #
    path('email_message/', EmailMessageListView.as_view(), name='mail_list'),
    path('email_message/create/', EmailMessageCreateView.as_view(), name='mail_create'),
    path('email_message/<int:pk>/update/', EmailMessageUpdateView.as_view(), name='mail_update'),
    path('email_message/<int:pk>/delete/', EmailMessageDeleteView.as_view(), name='mail_delete'),
]
