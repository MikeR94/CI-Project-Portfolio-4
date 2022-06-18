from django.test import TestCase
from django.urls import reverse, resolve
from home.views import gallery, index


class TestUrls(TestCase):
    """
    A class to test the home URLS
    """
    def test_home_url_is_resolved(self):
        """
        Tests if the home_now url is working
        correctly
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        url = reverse("home")
        self.assertEquals(resolve(url).func, index)
        self.assertTemplateUsed(response, "index.html")


    def test_gallery_url_is_resolved(self):
        """
        Tests if the gallery url is working
        correctly
        """
        response = self.client.get("/gallery")
        self.assertEqual(response.status_code, 200)

        url = reverse("gallery")
        self.assertEquals(resolve(url).func, gallery)
        self.assertTemplateUsed(response, "gallery.html")


    def test_wrong_uri_returns_404(self):
        """
        Tests if the 404 page is being rendered
        if an incorrect url is passed in
        """
        response = self.client.get('/something/different/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
