from django.test import TestCase
from django.urls import reverse, resolve
from Accounts.models import User
from Reviews.models import Review
from Reviews.views import create_review, show_single_review

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

    def test_review_id_url_is_resolve(self):
        response = self.client.get('/review/50')
        self.assertEqual(response.status_code, 404)
        self.user = User.objects.create_user(
            username="admin",
            password="adminadmin",
            email="admin@example.com",
            id = "50",
            )
        self.client.force_login(self.user)
        Review.objects.create(
            id = "50",
            user_id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            body = "hello",
        )
        response = self.client.get('/review/50')
        self.assertEqual(response.status_code, 200)

        url = reverse('single_review', kwargs={'review_id': '50'})
        self.assertEquals(resolve(url).func, show_single_review)
