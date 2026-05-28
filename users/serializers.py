from rest_framework import serializers
from .models import User


class UserLoginResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "rol"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UsuarioHistorialSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "nombre_completo",
            "telefono",
            "direccion",
            "ci",
            "rol"
        ]

    def get_nombre_completo(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()