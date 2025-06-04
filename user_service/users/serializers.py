from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Include password field for registration; it won't be exposed in responses
        fields = ['id', 'username', 'email', 'phone', 'address', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Hide password in serialized output
        }

    def create(self, validated_data):
        # Remove password from validated data so we can hash it manually
        password = validated_data.pop('password')

        # Create user instance without saving to the database yet
        user = User(**validated_data)

        # Use Django's secure password hashing
        user.set_password(password)

        # Save user to the database
        user.save()
        return user
