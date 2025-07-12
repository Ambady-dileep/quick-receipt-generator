from django.urls import path 
from . import views

urlpatterns = [
    path('api/test/',views.test_view),
    path('', views.home_view),
]