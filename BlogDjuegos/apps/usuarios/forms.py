from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required= True)
    First_name = forms.CharField(label='nombre', required=True)
    Last_name = forms.CharField(label='apellido', required= True)
    password1 = forms.CharField(
        label='contraseña', widget=forms.PasswordInput, required= True)
    password2 = forms.CharField(
        label='contraseña2', widget=forms.PasswordInput, required= True)


class meta:
    model = Usuario
    fields = [
        'First_name',
        'Last_name',
        'username',
        'password1',
        'password2',
    ]