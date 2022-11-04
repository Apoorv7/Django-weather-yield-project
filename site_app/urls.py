from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"weather", views.WeatherViewSet)
router.register(r"yield", views.YieldViewSet)


urlpatterns = [
    path("api/weather/stats", views.WeatherStats.as_view(), name="Weatherstats"),
    path("api/", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]
