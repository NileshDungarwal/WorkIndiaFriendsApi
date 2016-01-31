from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models.sector import Sector
from api.serializers.sectorserializer import SectorSerializer


# Create your views here.

@api_view(['get','post'])
def sector_list(request):
    if request.method == 'GET':
        sectors = Sector.objects.all().order_by('-created_at')
        sectors = SectorSerializer(sectors,many=True)
        print(sectors.data)
        return Response(sectors.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = SectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def sector_detail(request, pk):
    print(request.data)
    try:
        sector=Sector.objects.get(pk=pk)
    except Sector.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SectorSerializer(sector)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SectorSerializer(sector, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sector.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)