from django.db import models
from django.db.models import Sum, F, FloatField

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Receipt(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_total(self):
        return self.items.aggregate(
            total=Sum(F('quantity') * F('price'), output_field=FloatField())
        )['total'] or 0

    def __str__(self):
        return f"Receipt #{self.id} - {self.customer.name}"


class Item(models.Model):
    UNIT_CHOICES = [
        ('kg', 'kg'),
        ('g', 'g'),
        ('ltr', 'ltr'),
        ('ml', 'ml'),
        ('pcs', 'pcs'),
        ('box', 'box'),
        ('meter', 'meter'),
        ('dozen', 'dozen'),
        # add more as needed
    ]
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,related_name='items')
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='pcs')
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.quantity}*{self.name} - ₹{self.price}"
    


