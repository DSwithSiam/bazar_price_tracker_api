from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bazar.views import MarketViewSet, ItemViewSet, PriceViewSet, compare_prices, price_history
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import doc_view


# Initialize schema_view for Swagger documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Bazar Price Tracker API",
      default_version='v1',
      description="API documentation for the Bazar Price Tracker project",
      #terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="masipulislam@gmail.com"),
      license=openapi.License(name="Siam234234gh"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Router configuration
router = DefaultRouter()
router.register(r'markets', MarketViewSet)
router.register(r'items', ItemViewSet)
router.register(r'prices', PriceViewSet)

# URL patterns
urlpatterns = [
   path('', doc_view, name='doc'),
   path('api/', include(router.urls)),
   path('api/user/', include('users.urls')),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/compare/', compare_prices, name='compare_prices'),
   path('api/prices/<int:item_id>/history/', price_history, name='price_history'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)