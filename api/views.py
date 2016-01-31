from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['get'])
def test_api(request):
    return Response("API Tested")