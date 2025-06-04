from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_id = models.IntegerField()  # foreign key by reference
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
