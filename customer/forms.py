from django.forms import ModelForm
from .models import Customer, Inquiry

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['business_name', 'location', 'first_name', 'last_name','phone_number', 'inquiry']

class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = ['job_type', 'recorded_by', 'inspection_date', 'extra_details', 'approve_job']
