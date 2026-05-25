from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import User
from .serializers import UserSerializer, UserLoginResponseSerializer

from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginViewset(viewsets.ViewSet):

    def create(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({"error": "Credenciales inválidas"}, status=401)

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": UserLoginResponseSerializer(user).data,
            "token": str(refresh.access_token)
        })