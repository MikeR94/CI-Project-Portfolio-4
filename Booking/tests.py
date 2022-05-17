from django.test import TestCase
from django.urls import reverse, resolve
from Booking.views import book_now
from Home.views import index

class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        url = reverse('home')
        self.assertEquals(resolve(url).func, index)


    def test_book_now_is_resolved(self):
        response = self.client.get('/book-now')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_now')
        self.assertEquals(resolve(url).func, book_now)