from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #QUERY define que datos manejara la vista
    serializer_class = UserSerializer #SERIALIZER define como convertir esos datos a JSON