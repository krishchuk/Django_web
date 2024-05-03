from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from mail.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class CustomAuthenticationForm(StyleFormMixin, AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password',)


class ProfileChangeForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'full_name', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
