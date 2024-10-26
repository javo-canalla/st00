from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.forms.widgets import PasswordInput, TextInput

CustomUser = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'direccion_email', 'nombre', 'apellido',
                  'numero_telefono_particular', 'numero_de_interno', 'tipo_de_usuario')


class CustomPasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        UserModel = get_user_model()
        email_field_name = UserModel.get_email_field_name()
        kwargs = {
            f'{email_field_name}__iexact': email,
            'is_active': True,
        }
        return UserModel._default_manager.filter(**kwargs)


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Correo electrónico", max_length=254)

    def clean_email(self):
        email = self.cleaned_data['email']
        UserModel = get_user_model()
        if not UserModel.objects.filter(direccion_email__iexact=email, is_active=True).exists():
            raise forms.ValidationError(
                "No existe ninguna cuenta registrada con este correo electrónico.")
        return email


class CustomUserChangeForm(UserChangeForm):
    password = None  # Opcional: Ocultamos el campo de contraseña en este formulario

    class Meta:
        model = CustomUser
        fields = ('username', 'direccion_email', 'nombre', 'apellido',
                  'numero_telefono_particular', 'numero_de_interno', 'tipo_de_usuario')
