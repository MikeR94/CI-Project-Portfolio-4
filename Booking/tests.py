from django.test import TestCase
from django.urls import reverse, resolve
from Booking.models import Booking
from Booking.views import book_now

class TestUrls(TestCase):


    def test_book_now_is_resolved(self):
        response = self.client.get('/book-now')
        self.assertEqual(response.status_code, 200)

        url = reverse('book_now')
        self.assertEquals(resolve(url).func, book_now)


class TestModels(TestCase):
    def test_booking_model(self):
        """
        Testing Booking model is passing values correctly
        """
        order = Booking.objects.create(
            id = 50,
            first_name = "Mike",
            last_name = "Ralph",
            email = "mikeyralph@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07946472421"
        )

        self.assertEquals(order.id, 50)
        self.assertEquals(order.first_name, 'Mike')
        self.assertEquals(order.last_name, 'Ralph')
        self.assertEquals(order.email, 'mikeyralph@hotmail.co.uk')
        self.assertEquals(order.ref_number, '1234567890')
        self.assertEquals(order.date_of_visit, '2022-05-16')
        self.assertEquals(order.time_of_visit, '20:00:00')
        self.assertEquals(order.number_of_guests, '4')
        self.assertEquals(order.contact_number, '07946472421')