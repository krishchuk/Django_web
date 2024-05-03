from django.contrib import admin

from mail.models import Client, EmailSettings, EmailMessage, EmailTry


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment')
    search_fields = ('email', 'full_name')


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_datetime', 'periodicity', 'status')
    search_fields = ('first_datetime', 'status')
    list_filter = ('periodicity', 'status')


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'head', 'body')
    search_fields = ('head', 'body')


@admin.register(EmailTry)
class EmailTryAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_try_datetime', 'try_status', 'server_answer')
    search_fields = ('last_try_datetime', 'try_status')
    list_filter = ('try_status',)
