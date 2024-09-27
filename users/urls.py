from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarketManagerViewSet, CustomUserViewSet, LoginView, LogoutAPIView

router = DefaultRouter()
router.register(r'market_managers', MarketManagerViewSet, basename='marketmanager')
router.register(r'custom_users', CustomUserViewSet, basename='customuser')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)