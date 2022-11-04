from rest_framework import serializers
from .models import Weather, Yield, Results


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"


class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = "__all__"


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = "__all__"
