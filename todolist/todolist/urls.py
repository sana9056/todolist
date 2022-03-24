from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from userapp.viewsets import UserGenericViewSet
from todoapp.viewsets import todoappModelViewSet, todolistModelViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="todolist",
      default_version='0.1',
      description="Documentation to project",
      contact=openapi.Contact(email="sana9056@mail.ru"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('userapp', UserGenericViewSet)
router.register('todoapp', todoappModelViewSet)
router.register('todolist', todolistModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
