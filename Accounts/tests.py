from django.test import TestCase
from django.urls import reverse, resolve
from Accounts.views import show_user_reservations, user_details_booking
from Accounts.models import User

from Booking.models import Booking

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


    def test_user_details_booking_url_is_resolved(self):
        self.user = User.objects.create_user(
            username="admin",
            password="adminadmin",
            email="admin@example.com")
        self.client.force_login(self.user)
        Booking.objects.create(
            id = "1",
            first_name = "Mike",
            last_name = "Ralph",
            email = "mikeyralph@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07946472421"
        )
        response = self.client.get('/user-details-booking/1')
        self.assertEqual(response.status_code, 200)

        url = reverse('user_details_booking', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, user_details_booking)

