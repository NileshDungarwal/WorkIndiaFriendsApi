from django.db import models
from api.models.job import Job
from api.models.branch import Branch


class JobBranches(models.Model):
    job=models.ForeignKey(Job, related_name="branches")
    branch=models.ForeignKey(Branch, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)