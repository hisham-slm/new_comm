from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status


class TestSample(TestCase):
    
    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse('admin:index')
        res = self.client.get(url)
        print(res.data)

        self.assertEquals(res.status_code, 200)

        self.assertEquals(res.data, "Congratulations, you have created an API")