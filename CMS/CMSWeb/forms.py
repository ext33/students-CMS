from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class LoginForm(PlaceholderForm):
    username = forms.CharField(max_length=200, label='Login', help_text='Имя пользователя')
    password = forms.CharField(max_length=200, widget=forms.PasswordInput, help_text='Пароль')
