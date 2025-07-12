from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Customer,Receipt,Item 

# Create your views here.

def test_view(request):
    return JsonResponse({'message':"Hello from Django"})

def home_view(request):
    return HttpResponse("Welcome to the Quick Receipt Generator App!")

def customers_list(request):
    customers = Customer.objects.order_by('-created_at')
    context = {'customers':customers}
    return render(request,'receipts/customers_list.html',context)

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Customer.objects.create(name=name,email=email,phone=phone)
        return redirect('customers_list')
    return render(request,'receipts/add_customer.html')
