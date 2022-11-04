from django.shortcuts import render
from .serializers import WeatherSerializer, YieldSerializer, ResultsSerializer
from .models import Weather, Yield, Results
from rest_framework import viewsets, filters
from .models_data import YieldData, WeatherData, ResultsData
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    """
    Filters
    '' 
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "date", "station_id"]


class YieldViewSet(viewsets.ModelViewSet):
    queryset = Yield.objects.all()
    serializer_class = YieldSerializer
    """
    Filters
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["year"]


class WeatherStats(generics.ListCreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    """
    Filters
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["year", "station_id"]
