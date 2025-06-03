# Import base APIView class for handling HTTP requests
from rest_framework.views import APIView

# Import Response class to return structured API responses
from rest_framework.response import Response

# Import status codes for more readable and maintainable responses
from rest_framework import status

# Import Django's built-in user authentication function
from django.contrib.auth import authenticate

# Import the custom User model
from .models import User

# Import the serializer used to convert User objects to/from JSON
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        # Deserialize and validate incoming user data
        serializer = UserSerializer(data=request.data)

        # If data is valid, save the new user and return serialized data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If data is invalid, return errors with HTTP 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        # Extract username and password from the request body
        username = request.data.get('username')
        password = request.data.get('password')

        # Use Django's `authenticate` to verify credentials
        user = authenticate(username=username, password=password)

        if user:
            # Login successful
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

        # Login failed
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    def get(self, request):
        # Get the currently authenticated user
        user = request.user

        # Serialize user data to JSON
        serializer = UserSerializer(user)

        # Return user data
        return Response(serializer.data, status=status.HTTP_200_OK)
