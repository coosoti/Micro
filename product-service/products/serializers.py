# Import the serializers module from Django REST Framework
from rest_framework import serializers

# Import the Product model from the current app's models.py
from .models import Product


# Define a serializer class for the Product model
# A serializer converts model instances to JSON and validates input data
class ProductSerializer(serializers.ModelSerializer):

    # Meta class is used to provide metadata to the serializer
    class Meta:
        # Specifies the model that the serializer is based on
        model = Product

        # Use '__all__' to automatically include all fields from the Product model
        # You can also list fields explicitly like: ['id', 'name', 'description', 'price', 'stock']
        fields = "__all__"
