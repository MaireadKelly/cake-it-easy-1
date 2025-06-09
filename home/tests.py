from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_index_page_loads(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
