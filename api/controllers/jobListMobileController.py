from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models.job import Job
from api.models.jobbranches import JobBranches
from api.serializers.jobmobileserializer import JobMobileSerializer


@api_view(['get'])
def job_list(request):
    jobbranches = JobBranches.objects.all().order_by('-created_at')
    jobbranches = JobMobileSerializer(jobbranches,many=True)
    #print(jobs.data)
    return Response(jobbranches.data, status=status.HTTP_200_OK)
