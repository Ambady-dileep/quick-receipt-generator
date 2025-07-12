from django.urls import path 
from . import views

urlpatterns = [
    path('api/test/',views.test_view),
    path('', views.home_view),
    path('customers/', views.customers_list, name='customer_list'),
    path('customers/add/',views.add_customer, name='add_customer'),
]
