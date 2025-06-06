# Import Django's path function to define URL patterns
from django.urls import path

# Import the views that handle product-related requests
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

# Define the URL patterns for this app
urlpatterns = [
    # This route handles:
    # - GET /api/products/         → List all products
    # - POST /api/products/        → Create a new product
    path("", ProductListCreateView.as_view(), name="product-list-create"),
    # This route handles:
    # - GET /api/products/<id>/    → Retrieve details of a product
    # - PUT /api/products/<id>/    → Update a product
    # - DELETE /api/products/<id>/ → Delete a product
    # The <int:pk> part means it expects an integer primary key (id) in the URL
    path(
        "<int:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="product-detail"
    ),
]
