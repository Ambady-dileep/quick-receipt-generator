from django.urls import path 
from . import views

urlpatterns = [
    path('api/test/',views.test_view),
    path('', views.home_view),
    path('customers/', views.customers_list, name='customers_list'),
    path('customers/add/',views.add_customer, name='add_customer'),
    path('customers/<int:customer_id>/delete/',views.delete_customer, name='delete_customer'),
    path('receipts/form/', views.add_or_edit_receipt, name='add_receipt'),
    path('receipts/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('receipts/form/<int:receipt_id>/', views.add_or_edit_receipt, name='edit_receipt'),
    path('customers/<int:customer_id>/receipts/', views.customer_receipts, name='customer_receipts'),
    ]