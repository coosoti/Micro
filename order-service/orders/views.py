import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']

            # Step 1: Validate product from Product Service
            try:
                product_response = requests.get(f'http://product-service:8000/api/products/{product_id}/')
                if product_response.status_code != 200:
                    return Response({'error': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
            except requests.exceptions.RequestException:
                return Response({'error': 'Product service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            # Step 2: Reduce stock from Inventory Service
            try:
                inventory_response = requests.post(
                    f'http://inventory-service:8000/api/inventory/reduce-stock/',
                    json={'product_id': product_id, 'quantity': quantity}
                )
                if inventory_response.status_code != 200:
                    return Response({'error': 'Inventory update failed'}, status=inventory_response.status_code)
            except requests.exceptions.RequestException:
                return Response({'error': 'Inventory service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            order = serializer.save()
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
