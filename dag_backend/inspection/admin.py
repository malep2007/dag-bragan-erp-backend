from django.contrib import admin
from inspection.models import PropertyDetail, Surface

class PropertyDetailAdmin(admin.ModelAdmin):
    list_display = ('customer', 'property_type', 'services_required',)

class SurfaceAdmin(admin.ModelAdmin):
    list_display = ('surfaces', 'surface_area',)

admin.site.register(Surface, SurfaceAdmin)
admin.site.register(PropertyDetail, PropertyDetailAdmin)

# Register your models here.
