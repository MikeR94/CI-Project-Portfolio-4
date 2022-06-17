from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import (
    show_user_reservations,
    user_cancel_booking,
    user_details_booking,
)
from accounts.models import User
from booking.models import Booking


class TestUrls(TestCase):
    def test_user_reservations_url_is_resolved(self):
        """
        Test if the user reservations url is
        working correctly
        """
        response = self.client.get("/user-reservations")
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)
        response = self.client.get("/user-reservations")
        self.assertEqual(response.status_code, 200)

        url = reverse("user_reservations")
        self.assertEquals(resolve(url).func, show_user_reservations)
        self.assertTemplateUsed(response, "user_reservations.html")


    def test_user_details_booking_url_is_resolved(self):
        """
        Test if the user details booking url is
        working correctly
        """
        response = self.client.get("/user-details-booking/50")
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)
        Booking.objects.create(
            id="50",
            first_name="Mike",
            last_name="Ralph",
            email="testemail@hotmail.co.uk",
            ref_number="1234567890",
            date_of_visit="2022-05-16",
            time_of_visit="20:00:00",
            number_of_guests="4",
            contact_number="07436123635",
        )
        response = self.client.get("/user-details-booking/50")
        self.assertEqual(response.status_code, 200)

        url = reverse("user_details_booking", kwargs={"booking_id": "50"})
        self.assertEquals(resolve(url).func, user_details_booking)
        self.assertTemplateUsed(response, "user_details_booking.html")


    def test_user_details_booking_cancel_url_is_resolved(self):
        """
        Test if the user details cancel booking url is
        working correctly
        """
        response = self.client.get("/user-details-booking/cancel/50")
        self.assertEqual(response.status_code, 302)

        booking = Booking.objects.create(
            id="50",
            first_name="Mike",
            last_name="Ralph",
            email="testemail@hotmail.co.uk",
            ref_number="1234567890",
            date_of_visit="2022-05-16",
            time_of_visit="20:00:00",
            number_of_guests="4",
            contact_number="07436123635",
        )
        pk = booking.id
        retrieve_booking = Booking.objects.get(pk=booking.pk)
        self.assertTrue(Booking.objects.filter(pk=pk).exists())
        retrieve_booking.delete()
        self.assertFalse(Booking.objects.filter(pk=pk).exists())

        url = reverse("cancel", kwargs={"booking_id": "50"})
        self.assertEquals(resolve(url).func, user_cancel_booking)


class TestModels(TestCase):
    def test_user_account(self):
        """
        Testing user account is accepting correct values
        """
        user = User.objects.create(
            first_name="Mike",
            last_name="Ralph",
            id=1,
            username="Mike",
            email="testemail@hotmail.co.uk",
            is_active=True,
            is_staff=False,
        )

        self.assertEquals(user.first_name, "Mike")
        self.assertEquals(user.last_name, "Ralph")
        self.assertEquals(user.id, 1)
        self.assertEquals(user.username, "Mike")
        self.assertEquals(user.email, "testemail@hotmail.co.uk")
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_staff, False)


    def test_staff_account(self):
        """
        Testing staff account is accepting correct values
        """
        admin = User.objects.create(
            first_name="Mike",
            last_name="Ralph",
            id=1,
            username="Mike",
            email="testemail@hotmail.co.uk",
            is_active=True,
            is_staff=True,
        )

        self.assertEquals(admin.first_name, "Mike")
        self.assertEquals(admin.last_name, "Ralph")
        self.assertEquals(admin.id, 1)
        self.assertEquals(admin.username, "Mike")
        self.assertEquals(admin.email, "testemail@hotmail.co.uk")
        self.assertEquals(admin.is_active, True)
        self.assertEquals(admin.is_staff, True)
