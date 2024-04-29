from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.

class TrackingViewSet(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = packSerializer
    filter_backends = [DjangoFilterBackend]#, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["trackingNumber","carrier"]