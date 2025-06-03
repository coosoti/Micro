# Import the serializers module from Django REST Framework
from rest_framework import serializers

# Import the custom User model from the same app
from .models import User

# Define a serializer for the custom User model
class UserSerializer(serializers.ModelSerializer):
    # Meta class provides metadata about the serializer
    class Meta:
        # Link the serializer to the User model
        model = User

        # Specify the model fields to be included in the serialized output
        # 'id' is typically an auto-generated primary key
        fields = ['id', 'username', 'email', 'phone', 'address']
