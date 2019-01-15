from django.db import models
from customer.models import Customer
from django.contrib.auth.models import User


class Surface(models.Model):
    SURFACES = (
        ('1', 'Ceramic'),
        ('2', 'Porcelain'),
        ('3', 'Granite'),
        ('4', 'Grass'),
        ('5', 'Marble'),
        ('6', 'Terazzo'),
        ('7', 'Wood'),
        ('8', 'Trees'),
        ('9','Carpet'),
        ('10', 'PVC/ Vinly'),
        ('11', 'Rubber'),
        ('12', 'Flower Bed'),
        ('13', 'Paint'),
        ('14', 'Steel'),
        ('15', 'Cement'),
        ('16', 'Hedge'),
    )
    surfaces = models.CharField(max_length=12, null=True, choices=SURFACES)
    surface_area = models.IntegerField(null=True)
    others = models.CharField(max_length=12, null=True)

    def __str__(self):
        if self.surfaces:
            return "{0} {1} sqm".format(self.surfaces, self.surface_area)
        elif self.others:
            return "{0} {1} sqm".format(self.others, self.surface_area)
        else:
            return "N/A"

class Pest(models.Model):
    PESTS = (
        ('1', 'Mosquitoes'),
        ('2', 'Cockroaches'),
        ('3', 'Bats'),
        ('4', 'Rodents'),
        ('5', 'Bed bugs'),
        ('6', 'Termites'),
        ('7', 'Snakes'),
        ('8', 'Lizards'),
        ('9', 'Fleas'),
        ('10', 'Others')
    )
    pest_type = models.CharField(max_length=12, null=True, choices=PESTS)
    others_specify = models.CharField(max_length=12, null=True)

    def __str__(self):
        if self.pest_type:
            return "{}".format(self.pest_type)
        else:
            return "{}".format(self.others_specify)

class PropertyDetail(models.Model):
    PROP_TYPE = (
        ('PR', 'Public Residential'),
        ('PC', 'Public Commercial'),
        ('FP', 'Food Preparation'),
        ('WH', 'Warehouse/ Store'),
        ('PvR', 'Private Residential'),
        ('O', 'Others/ Specify')
    )

    SERVICES = (
        ('C', 'Cleaning'),
        ('G', 'Gardening'),
        ('PC', 'Pest Control')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    recodered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    property_type = models.CharField(
        max_length=12, choices=PROP_TYPE, default='Public Residential')
    services_required = models.CharField(
        max_length=12, choices=SERVICES, default='Cleaning')
    number_of_floors = models.IntegerField(null=True)
    estimated_area = models.IntegerField(null=True)
    number_of_occupants = models.IntegerField(null=True)
    description_of_terrain = models.TextField(null=True)
    surface = models.ForeignKey(Surface, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{0} {1}".format(self.customer, self.property_type)

    def get_absolute_url(self):
        return reverse("inspection:detail", kwargs={"pk": self.pk})

