from django.test import TestCase
from django.urls import reverse, resolve
from Booking.views import book_now

class TestUrls(TestCase):


    def test_book_now_is_resolved(self):
        response = self.client.get('/book-now')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_now')
        self.assertEquals(resolve(url).func, book_now)