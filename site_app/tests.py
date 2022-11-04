from rest_framework.test import APITestCase
from rest_framework import status


class Tests(APITestCase):
    def test_check(self):

        url_weather = "http://127.0.0.1:8000/api/weather/"
        response = self.client.get(url_weather, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url_yield = "http://127.0.0.1:8000/api/yield/"
        response = self.client.get(url_yield, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url_result = "http://127.0.0.1:8000/api/weather/stats"
        response = self.client.get(url_result, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
