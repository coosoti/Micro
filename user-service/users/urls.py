# Import the path function for defining URL routes
from django.urls import path

# Import the views for registration, login, and profile
from .views import RegisterView, LoginView, ProfileView

# Define URL patterns for the users app
urlpatterns = [
    path(
        "register/", RegisterView.as_view(), name="register"
    ),  # POST endpoint for user registration
    path("login/", LoginView.as_view(), name="login"),  # POST endpoint for user login
    path(
        "profile/", ProfileView.as_view(), name="profile"
    ),  # GET endpoint to fetch logged-in user's profile
]
