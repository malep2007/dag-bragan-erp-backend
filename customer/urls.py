from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='index'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name="detail"),
    path('edit/<int:pk>/', views.CustomerUpdateView.as_view(), name='edit'),
    path('add/', views.CustomerCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='delete'),
]
