from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarketManagerViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'market_managers', MarketManagerViewSet, basename='marketmanager')
router.register(r'custom_users', CustomUserViewSet, basename='customuser')


urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)