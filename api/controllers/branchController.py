from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models.company import Company
from api.models.branch import Branch
from api.serializers.companyserializer import CompanySerializer
from api.serializers.branchserializer import BranchSerializer


# Create your views here.

@api_view(['get','post'])
def branch_list(request, companyId):
    #print(request.data)
    company = Company.objects.get(pk=companyId)
    if request.method == 'GET':
        branches = company.branches.all().order_by('-created_at')
        branches = BranchSerializer(branches,many=True)
        print(branches.data)
        print("hello")
        return Response(branches.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BranchSerializer(data=request.data,context={
            "company": company
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def branch_detail(request, companyId, branchId):
    # print(request.data)
    try:
        company=Company.objects.get(pk=companyId)
        branch=company.branches.get(pk=branchId)
    except Company.DoesNotExist or Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        print(branch)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)