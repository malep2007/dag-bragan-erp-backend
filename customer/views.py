from django.views import generic
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Customer, Inquiry
from .forms import InquiryForm, CustomerForm


def customer_list(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        customers = Customer.objects.all()
        context = {"customers": customers, "title": "Customer List"}
        return render(request, "customer/customer_list.html", context)


@login_required(login_url="/login/")
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
