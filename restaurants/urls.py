from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'', RestauranteViewSet) #restaurantes
router.register(r'', ProductoViewSet) #productos

urlpatterns = router.urls
