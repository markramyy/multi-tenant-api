from django.urls import path, include

from .views import tenant_list, create_tenant

from rest_framework.routers import DefaultRouter
from .api import TenantViewSet

router = DefaultRouter()
router.register('tenants', TenantViewSet, basename='tenant')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', tenant_list, name='tenant_list'),
    path('create/', create_tenant, name='create_tenant'),
]
