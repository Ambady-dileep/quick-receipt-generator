from django.db import models

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

class Item(models.Model):
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,related_name='items')
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.quantity}*{self.name} - ₹{self.price}"
    


