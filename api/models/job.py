from django.db import models
from api.models.branch import Branch
from api.models.sector import Sector

class Job(models.Model):
    designation = models.CharField(max_length=100)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    shift_timing = models.CharField(max_length=100, blank=True)
    sector = models.ForeignKey(Sector, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'