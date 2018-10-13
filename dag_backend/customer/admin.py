from django.contrib import admin
from django.contrib.admin import AdminSite

from customer.models import Customer, Inquiry

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('business_name','full_name', 'inquiry','phone_number','location', )
    list_editable = ('location',)
    list_filter = ('business_name', 'location')
    search_fields =('business_name', 'first_name',)


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('inq_number','job_type', 'inspection_date', 'recorded_by','approve_job',)
    list_filter = ('inq_number','job_type')
    list_editable=('approve_job',)
    search_fields = ('inq_number',)

class MyAdminSite(AdminSite):
    """Custom site configuration for admin panel"""
    site_header = 'Dag & Bragan'

#create a my_site urls path to use in urls configuration
my_site = MyAdminSite(name = 'dag-admin')

#register your models on the customised admin site
my_site.register(Customer, CustomerAdmin)
my_site.register(Inquiry, InquiryAdmin)

# Register your models here.
