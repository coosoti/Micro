from django.urls import path
from .views import InventoryListCreateView, InventoryRetrieveUpdateDestroyView, ReduceStockView

urlpatterns = [
    path("", InventoryListCreateView.as_view(), name="inventory-list-create"),
    path(
        "<int:pk>/",
        InventoryRetrieveUpdateDestroyView.as_view(),
        name="inventory-detail",
    ),
    path('reduce-stock/', ReduceStockView.as_view(), name='reduce-stock'),
]
