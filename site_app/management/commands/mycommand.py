from django.core.management.base import BaseCommand
from ...models_data import WeatherData, YieldData, ResultsData


class Command(BaseCommand):
    def handle(self, *args, **options):
        WeatherData()
        YieldData()
        ResultsData()
