from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.

def test_view(request):
    return JsonResponse({'message':"Hello from Django"})

def home_view(request):
    return HttpResponse("Welcome to the Quick Receipt Generator App!")