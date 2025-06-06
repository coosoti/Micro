# Import the base Django User model that provides built-in authentication features
from django.contrib.auth.models import AbstractUser

# Import Django's base model class to define database models
from django.db import models


# Define a custom user model by extending Django's built-in AbstractUser
class User(AbstractUser):
    # Add a phone number field to the user model
    # CharField is used for text-based input (max 15 characters)
    # blank=True allows the field to be left empty in forms
    # null=True allows the field to store NULL in the database if no value is provided
    phone = models.CharField(max_length=15, blank=True, null=True)

    # Add an address field to the user model
    # TextField is suitable for longer text inputs
    # Both blank=True and null=True make the field optional
    address = models.TextField(blank=True, null=True)

    # String representation of the user instance
    # When the object is printed (e.g., in the admin dashboard), this value will be shown
    def __str__(self):
        return self.username  # username is inherited from AbstractUser
