from django.contrib import admin
from .models import Customer, Receipt, Item

# Register your models here.
admin.site.register(Customer)
admin.site.register(Receipt)
admin.site.register(Item)

