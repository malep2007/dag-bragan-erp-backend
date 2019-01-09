# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import generics, mixins
# from customer.models import Customer, Inquiry
# from customer.serializer import CustomerSerializer, InquirySerializer

# # Create your views here.
# class CustomerList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # def post(self, request, *args, **kwargs):
#     #     return self.create(request, *args, *kwargs)

# class CustomerDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
#     ):

#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class InquiryList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
#     ):
#     queryset = Inquiry.objects.all()
#     serializer_class = InquirySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class InquiryDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView):

#     queryset = Inquiry.objects.all()
#     serializer_class = InquirySerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

from django.views import generic
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from .models import Customer, Inquiry
from .forms import InquiryForm, CustomerForm


def customer_list(request):
    customers = Customer.objects.all()
    context = {"customers": customers, "title":"Customer List"}
    return render(request, "customer/customer_list.html", context)

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    initial_data = {
        'business_name': customer.business_name,
        'location': customer.location,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'phone_number': customer.phone_number,
        'inquiry': customer.inquiry
    }
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form = CustomerForm(form.cleaned_data)
            form.save()
            return render(request, "customer/customer_detail.html", {
            "form": form,
            "customer": customer,
            "title": "Customer Detail"
        })
    else:
        form = CustomerForm(initial=initial_data)
    return render(request, "customer/customer_detail.html", {
        "form": form,
        "customer": customer,
        "title": "Customer Detail"
    })

def customer_add(request):
    form = CustomerForm()
    context = {
            "title": "Add Customer",
            "form": form
        }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            Customer.objects.create(**request.POST)
            return HttpResponseRedirect("customer: index")
    else:
        form = CustomerForm()
    return render(request, "customer/customer_add.html", context)

def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return redirect("customer:index")
