from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=100)
    sectors = models.ManyToManyField('Sector', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'