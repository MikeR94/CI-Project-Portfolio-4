from django.test import TestCase
from django.urls import reverse, resolve
from Home.views import gallery, index

class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        url = reverse('home')
        self.assertEquals(resolve(url).func, index)


    def test_gallery_url_is_resolved(self):
        response = self.client.get('/gallery')
        self.assertEqual(response.status_code, 200)

        url = reverse('gallery')
        self.assertEquals(resolve(url).func, gallery)
