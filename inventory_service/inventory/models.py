from django.db import models

class Inventory(models.Model):
    product_id = models.IntegerField()  # Reference to Product (cross-service communication)
    quantity = models.PositiveIntegerField()  # Quantity in stock

    def __str__(self):
        return f"Product ID: {self.product_id}, Quantity: {self.quantity}"
