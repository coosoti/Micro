from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer

# Handles listing all inventory items and creating new ones
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# Handles retrieving, updating, and deleting a specific inventory item
class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
