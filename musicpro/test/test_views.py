from django.test import TestCase, Client
from django.urls import reverse
from musicpro.models import *
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.catalogo_url = reverse('catalogo')

    def test_project_catalogo_GET(self):
        response = self.client.get(self.catalogo_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'template/catalogo.html')

