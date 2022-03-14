from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from userapp.viewsets import UserGenericViewSet
from todoapp.viewsets import todoappModelViewSet, todolistModelViewSet


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
]
