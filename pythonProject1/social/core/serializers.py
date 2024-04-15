from rest_framework import serializers
from .models import CustomUser, Message


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        models = CustomUser
        fields = ['id', 'username', 'mensajes_pasados', 'likes_recibidos_globales', 'nombre']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        models = Message
        fields = ['id', 'content', 'latitude', 'longitude', 'created_at', 'likes_recibidos', 'usuario']


