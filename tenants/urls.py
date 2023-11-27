from django.urls import path

from .views import tenant_list, create_tenant


urlpatterns = [
    path('', tenant_list, name='tenant_list'),
    path('create/', create_tenant, name='create_tenant'),
]
