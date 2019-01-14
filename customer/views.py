from django.views import generic
from backends.backend import Backend
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Customer, Inquiry
from .forms import InquiryForm, CustomerForm


class CustomerListView(generic.ListView):
    model = Customer
    context_template_name = "customer/customer_list.html"
    context_object_name = 'customers'

class CustomerDetailView(generic.DetailView):
    model = Customer

class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = [
        'business_name', 'location',
        'first_name', 'last_name','phone_number'
    ]

class CustomerCreateView(generic.CreateView):
    model = Customer
    fields = [
        'business_name', 'location',
        'first_name', 'last_name','phone_number'
    ]

class CustomerDeleteView(generic.DeleteView):
    model = Customer
    context_template_name = "customer/customer_confirm_delete.html"
    context_object_name = 'customer'

    def get_success_url(self):
        return reverse('customer:index')
