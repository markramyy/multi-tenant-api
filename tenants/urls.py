from django.urls import path
from django.contrib import admin
from .views import tenant_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tenant_list, name='tenant_list'),
]