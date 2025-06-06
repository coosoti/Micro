# Import generic class-based views from Django REST Framework
from rest_framework import generics

# Import the Product model and serializer
from .models import Product
from .serializers import ProductSerializer


# This view handles two operations:
# 1. GET: List all products
# 2. POST: Create a new product
# It uses the ListCreateAPIView, which provides both listing and creation in one view
class ProductListCreateView(generics.ListCreateAPIView):
    # Define the queryset: all Product objects from the database
    queryset = Product.objects.all()

    # Specify the serializer class that converts Product objects to/from JSON
    serializer_class = ProductSerializer


# This view handles three operations for a single product (identified by its ID):
# 1. GET: Retrieve details of a product
# 2. PUT/PATCH: Update a product
# 3. DELETE: Delete a product
# It uses RetrieveUpdateDestroyAPIView which provides all three actions
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Define the queryset for looking up Product instances
    queryset = Product.objects.all()

    # Use the ProductSerializer to serialize/deserialize Product data
    serializer_class = ProductSerializer
