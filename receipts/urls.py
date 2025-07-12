from django.urls import path 
from . import views

urlpatterns = [
    path('api/test/',views.test_view),
    path('', views.home_view),
    path('customers/', views.customers_list, name='customers_list'),
    path('customers/add/',views.add_customer, name='add_customer'),
    path('customers/<int:customer_id>/delete/',views.delete_customer, name='delete_customer'),
]
