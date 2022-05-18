from django.test import TestCase
from django.urls import reverse, resolve
from Accounts.views import show_user_reservations
from Accounts.models import User
from django.test import Client

class TestUrls(TestCase):

    def test_user_reservations_url_is_resolved(self):
        self.user = User.objects.create_user(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
        response = self.client.get('/user-reservations')
        self.assertEqual(response.status_code, 200)

        url = reverse('user_reservations')
        self.assertEquals(resolve(url).func, show_user_reservations)

