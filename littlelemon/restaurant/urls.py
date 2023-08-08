from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, CategoryViewSet, OrderViewSet, MyObtainTokenPairView, RegisterView,ReservationViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
   
]
