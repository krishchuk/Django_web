from django import forms
from django.forms import BooleanField

from mail.models import Client, EmailSettings, EmailMessage
from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'full_name', 'comment',)


class EmailSettingsForms(StyleFormMixin, forms.ModelForm):
    # def __init__(self, owner=None, *args, **kwargs):
    #     super(EmailSettingsForms, self).__init__(*args, **kwargs)
    #     self.fields['clients'].queryset = Client.objects.filter(owner=owner)
    #     self.fields['message'].queryset = EmailMessage.objects.filter(owner=owner)

    class Meta:
        model = EmailSettings
        fields = ('periodicity', 'message', 'clients', 'date_start', 'date_end')


class EmailMessageForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ('head', 'body',)
