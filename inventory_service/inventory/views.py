from rest_framework import generics
#from .models import Inventory
from .serializers import InventorySerializer

# inventory/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory

class ReduceStockView(APIView):
    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")

        if not product_id or not quantity:
            return Response({"error": "product_id and quantity are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            inventory_item = Inventory.objects.get(product_id=product_id)
            if inventory_item.quantity < quantity:
                return Response({"error": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)

            inventory_item.quantity -= quantity
            inventory_item.save()
            return Response({"message": "Stock updated"}, status=status.HTTP_200_OK)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory item not found"}, status=status.HTTP_404_NOT_FOUND)


# Handles listing all inventory items and creating new ones
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# Handles retrieving, updating, and deleting a specific inventory item
class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
