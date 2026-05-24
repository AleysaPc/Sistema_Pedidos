from rest_framework.routers import DefaultRouter
from .views import OrdenViewSet, DetalleOrdenViewSet, Historial_ordenViewSet, NotificacionViewSet

router = DefaultRouter()
router.register(r'ordenes', OrdenViewSet) #ordenes
router.register(r'detalleordenes', DetalleOrdenViewSet) #detalleordenes
router.register(r'historialordenes', Historial_ordenViewSet) #historialordenes
router.register(r'notificaciones', NotificacionViewSet)

urlpatterns = router.urls