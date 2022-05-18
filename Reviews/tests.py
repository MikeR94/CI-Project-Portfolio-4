from django.test import TestCase
from django.urls import reverse, resolve
from Accounts.models import User
from Reviews.views import create_review

class TestUrls(TestCase):

    def test_create_review_url_is_resolved(self):
        response = self.client.get('/create/review')
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
        response = self.client.get('/create/review')
        self.assertEqual(response.status_code, 200)

        url = reverse('create_review')
        self.assertEquals(resolve(url).func, create_review)
