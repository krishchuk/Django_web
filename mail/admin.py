from django.contrib import admin

from mail.models import Client, EmailSettings, EmailMessage, EmailTry


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment', 'owner')
    search_fields = ('email', 'full_name')


@admin.register(EmailSettings)
class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start', 'date_end', 'periodicity', 'status', 'owner', 'is_active')
    search_fields = ('date_start', 'status')
    list_filter = ('periodicity', 'status')


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'head', 'body', 'owner')
    search_fields = ('head', 'body')


@admin.register(EmailTry)
class EmailTryAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_try_datetime', 'try_status', 'server_answer')
    search_fields = ('last_try_datetime', 'try_status')
    list_filter = ('try_status',)
