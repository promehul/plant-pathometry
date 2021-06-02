from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from pathology.models import Plant
from pathology.serializers import PlantSerializer

from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404



class PlantView(APIView):
    
    def get(self, request):
        lk = request.GET.get("lk", "")
        plant_object = get_object_or_404(Plant, lk= lk)
       
        if (plant_object is None):
           plant_object = Plant.objects.get(lk="apple_healthy")
        
        serializer = PlantSerializer(plant_object)
        return Response(serializer.data)
