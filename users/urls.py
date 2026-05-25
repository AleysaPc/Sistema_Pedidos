from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewset
from django.urls import path


router = DefaultRouter()
router.register(r'users', UserViewSet) #users

login_view = LoginViewset.as_view({'post': 'create'})

urlpatterns = [
    path('login/', login_view, name='login'),
]
# urlpatterns = router.urls