from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet) #restaurantes
router.register(r'productos', ProductoViewSet) #productos

urlpatterns = router.urls
