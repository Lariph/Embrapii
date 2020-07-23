from django.shortcuts import render
from rest_framework import generics
from .models import Pacient
from .serializers import PacientSerializer

class PacientList(generics.ListCreateAPIView):
    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer