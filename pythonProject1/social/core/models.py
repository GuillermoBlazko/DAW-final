from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    mensajes_pasados = models.ManyToManyField('Message', related_name='usuarios_mensaje_pasado', blank=True)
    likes_recibidos = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100)

    # Specify unique related_name for groups
    grupos = models.ManyToManyField('auth.Group', related_name='grupos_custom_permisos')
    # Specify unique related_name for user_permissions
    permisos = models.ManyToManyField('auth.Permission', related_name='usuarios_custom_permisos')

    def __str__(self):
        return self.username


class Message(models.Model):
    content = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="mensajes")

    def __str__(self):
        return f'Mensaje del usuario {self.usuario.username} - "{self.content}" - {self.created_at} - {self.likes}'
