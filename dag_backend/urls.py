"""dag_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
# from customer.admin import my_site

urlpatterns = [
    path('', views.index, name='home'),
    path('customer/',include(('customer.urls','customer'), namespace='customer')),
    path('inspection/', include(('inspection.urls','inspection'), namespace='inspection')),
    path('admin/', admin.site.urls),
    # path('admin/', my_site.urls),
]
