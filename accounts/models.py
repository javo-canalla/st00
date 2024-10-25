from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class TipoUsuario(models.TextChoices):
    ADMINISTRADOR = 'administrador', 'Administrador'
    COMUN = 'comun', 'Común'
    OPERARIO = 'operario', 'Operario'
    SUPERVISOR = 'supervisor', 'Supervisor'

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion_email = models.EmailField(unique=True)
    numero_telefono_particular = models.CharField(max_length=15)
    numero_de_interno = models.CharField(max_length=10)
    tipo_de_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.COMUN,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['direccion_email', 'nombre', 'apellido']

    def __str__(self):
        return f"{self.username} ({self.tipo_de_usuario})"
