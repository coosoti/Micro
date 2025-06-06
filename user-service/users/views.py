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

from rest_framework.authtoken.models import Token

# Import DRF's built-in permission class to restrict access to authenticated users only
from rest_framework.permissions import IsAuthenticated


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


# class LoginView(APIView):
#   def post(self, request):
# Extract username and password from the request body
#      username = request.data.get('username')
#     password = request.data.get('password')

# Use Django's `authenticate` to verify credentials
#    user = authenticate(username=username, password=password)

#   if user:
# Login successful
#      return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

# Login failed
# return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(APIView):
    # This method handles POST requests for user login
    def post(self, request):
        # Extract username and password from the incoming request data (JSON body)
        username = request.data.get("username")
        password = request.data.get("password")

        # Use Django's built-in authentication system to verify credentials
        user = authenticate(username=username, password=password)

        # If authentication is successful (user is not None)
        if user:
            # Get or create an authentication token for this user
            # If a token already exists for the user, it will be reused
            token, created = Token.objects.get_or_create(user=user)

            # Return the token in the response with HTTP 200 OK
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        # If authentication fails (user is None), return an error response
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class ProfileView(APIView):

    # Only allow access to this view if the user is authenticated
    # This prevents anonymous users from accessing the profile endpoint
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the currently authenticated user
        user = request.user

        # Serialize user data to JSON
        serializer = UserSerializer(user)

        # Return user data
        return Response(serializer.data, status=status.HTTP_200_OK)
