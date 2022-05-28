from django.shortcuts import render
from rest_framework import viewsets
from . serializers import foodsSerializer
from . models import foods   

# Create your views here.

class foodviewset(viewsets.ModelViewSet):
    queryset = foods.objects.all().order_by('Name')
    serializer_class = foodsSerializer