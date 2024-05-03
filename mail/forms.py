from django import forms
from django.forms import BooleanField

from mail.models import Client, EmailSettings, EmailMessage


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
    class Meta:
        model = EmailSettings
        fields = ('periodicity', 'status',)


class EmailMessageForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ('head', 'body',)
