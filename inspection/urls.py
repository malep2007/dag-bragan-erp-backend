from django.urls import path
from . import views

urlpatterns = [
    path('', views.PropertyDetailList.as_view(), name='index'),
    path('detail/<int:pk>', views.PropertyDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.PropertyUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.PropertyDeleteView.as_view(), name='delete'),
    path('create/', views.PropertyCreateView.as_view(), name='create'),
]
