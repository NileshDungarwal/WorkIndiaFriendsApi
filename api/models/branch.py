from django.db import models
from api.models.company import Company
from api.models.location import Location

class Branch(models.Model):
    address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='branches')
    location = models.ForeignKey(Location, related_name='branches')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'