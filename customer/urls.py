from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='index'),
    path('<int:pk>/', views.customer_detail, name="detail"),
    path('add/', views.customer_add, name='customer_add')
]
