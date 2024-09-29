from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationApiView, UserLoginApiView, UserLogoutView, UserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename = 'profile')
router.register('data', UserViewSet, basename = 'data')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)