from rest_framework.routers import DefaultRouter
from .views import OrdenViewSet, DetalleOrdenViewSet, Historial_ordenViewSet

router = DefaultRouter()
router.register(r'', OrdenViewSet) #ordenes
router.register(r'', DetalleOrdenViewSet) #detalleordenes
router.register(r'', Historial_ordenViewSet) #historialordenes

urlpatterns = router.urls