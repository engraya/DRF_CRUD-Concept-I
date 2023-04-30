from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tour
from .serializers import TourSerializer



@api_view(['GET'])
def tourList(request):
    tour = Tour.objects.all()
    serializer = TourSerializer(tour, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def tourDetail(request, pk):
    tour = Tour.objects.get(id=pk)
    serializer = TourSerializer(tour)
    return Response(serializer.data)


@api_view(['POST'])
def tourCreate(request):
    serializer = TourSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def tourUpdate(request, pk):
    tour = Tour.objects.get(id=pk)
    serializer = TourSerializer(instance=tour, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def tourDelete(request, pk):
    tour = Tour.objects.get(id=pk)
    tour.delete()

    return Response(serializer.data)

