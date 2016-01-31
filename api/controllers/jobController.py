from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models.job import Job
from api.models.branch import Branch
from api.models.jobbranches import JobBranches
from api.serializers.jobserializer import JobSerializer


# Create your views here.

@api_view(['get','post'])
def job_list(request):
    if request.method == 'GET':
        jobs = Job.objects.all().order_by('-created_at')
        jobs = JobSerializer(jobs,many=True)
        #print(jobs.data)
        return Response(jobs.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        #print(request.data)
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # for branch in request.data.branches:
            #     print(branch.address)
                #b = Branch.objects.get(id=branch['id'])
                #jobBranches = JobBranches.objects.create(job=,branch=b)
                #jobBranches.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, pk):
    print(request.data)
    try:
        job=Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)