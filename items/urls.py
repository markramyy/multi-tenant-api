from django.urls import path

from .views import item_list, item_detail, item_create

urlpatterns = [
    path('', item_list, name='item_list'),
    path('<int:id>/', item_detail, name='item_detail'),
    path('create/', item_create, name='item_create'),
]
