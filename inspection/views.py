from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import PropertyDetail


class PropertyDetailList(generic.ListView):
    model = PropertyDetail
    context_template_name = "inpection/inspection_detail.html"
    context_object_name = "property_details"

class PropertyDetailView(generic.DetailView):
    model = PropertyDetail
    context_object_name = 'property_detail'

class PropertyUpdateView(generic.UpdateView):
    model = PropertyDetail
    fields = ['customer', 'recodered_by', 'property_type', 'services_required']
    context_object_name = 'property_detail'

class PropertyCreateView(generic.CreateView):
    model = PropertyDetail
    fields = ['customer', 'recodered_by', 'property_type', 'services_required']


class PropertyDeleteView(generic.DeleteView):
    model = PropertyDetail
    context_object_name = 'property_detail'
