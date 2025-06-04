from django.urls import path
from .views import InventoryListCreateView, InventoryRetrieveUpdateDestroyView

urlpatterns = [
    path('', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('<int:pk>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
]
