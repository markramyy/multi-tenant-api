from django.urls import path,include

from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

from rest_framework.routers import DefaultRouter
from .api import ItemViewSet

router = DefaultRouter()
router.register('items', ItemViewSet, basename='item')

urlpatterns = [
    path('api/', include(router.urls)),

    path('', ItemListView.as_view(), name='item_list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item_update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
