from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, resolve
from accounts.models import User
from booking.models import Booking
from booking.views import book_now
from booking.forms import BookingForm


class TestUrls(TestCase):
    def test_book_now_is_resolved(self):
        response = self.client.get("/book-now")
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)
        response = self.client.get("/book-now")
        self.assertEqual(response.status_code, 200)

        url = reverse("book_now")
        self.assertEquals(resolve(url).func, book_now)
        self.assertTemplateUsed(response, "book_now.html")


class TestModels(TestCase):
    def test_booking_model(self):
        """
        Testing Booking model is passing values correctly
        """
        order = Booking.objects.create(
            id=50,
            first_name="Mike",
            last_name="Ralph",
            email="testemail@hotmail.co.uk",
            ref_number="1234567890",
            date_of_visit="2022-05-16",
            time_of_visit="20:00:00",
            number_of_guests="4",
            contact_number="07436123635",
            guest_attended=False,
            guest_no_show=False,
            booking_approved=False,
            booking_denied=False,
            booking_acknowledged=False,
        )

        self.assertEquals(order.id, 50)
        self.assertEquals(order.first_name, "Mike")
        self.assertEquals(order.last_name, "Ralph")
        self.assertEquals(order.email, "testemail@hotmail.co.uk")
        self.assertEquals(order.ref_number, "1234567890")
        self.assertEquals(order.date_of_visit, "2022-05-16")
        self.assertEquals(order.time_of_visit, "20:00:00")
        self.assertEquals(order.number_of_guests, "4")
        self.assertEquals(order.contact_number, "07436123635")
        self.assertEquals(order.guest_attended, False)
        self.assertEquals(order.guest_no_show, False)
        self.assertEquals(order.booking_approved, False)
        self.assertEquals(order.booking_denied, False)
        self.assertEquals(order.booking_acknowledged, False)


class TestForms(TestCase):
    def test_booking_form(self):
        """
        Testing booking form is accepting correct values
        """
        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)

        form = BookingForm(
            data={
                "first_name": "Mike",
                "last_name": "Ralph",
                "email": "testemail@hotmail.com",
                "time_of_visit": "18:00:00",
                "date_of_visit": "2022-12-01",
                "number_of_guests": "4",
                "contact_number": "07456 789 342",
                "additional_info": "N/A",
                "disabled_access": False,
            }
        )
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("time_of_visit", form.fields)
        self.assertIn("date_of_visit", form.fields)
        self.assertIn("number_of_guests", form.fields)
        self.assertIn("contact_number", form.fields)
        self.assertIn("additional_info", form.fields)
        self.assertIn("disabled_access", form.fields)

        request = HttpRequest()
        request.POST = {
            "first_name": "Mike",
            "last_name": "Ralph",
            "email": "testemail@hotmail.com",
            "time_of_visit": "18:00:00",
            "date_of_visit": "2022-12-01",
            "number_of_guests": "4",
            "contact_number": "07456 789 342",
            "additional_info": "N/A",
            "disabled_access": False,
        }
        test_form = BookingForm(request.POST)
        self.assertTrue(test_form.is_valid())

    def test_booking_form_date_of_visit_errors(self):
        """
        Testing booking form is throwing errors for incorrect correct values
        """
        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)

        request = HttpRequest()
        request.POST = {
            "first_name": "Mike",
            "last_name": "Ralph",
            "email": "testemail@hotmail.com",
            "time_of_visit": "07:00:00",
            "date_of_visit": "2021-12-01",
            "number_of_guests": "4",
            "contact_number": "07456 789 342",
            "additional_info": "N/A",
            "disabled_access": False,
        }
        test_form = BookingForm(request.POST)
        self.assertFalse(test_form.is_valid())
        self.assertEqual(
            test_form.errors["date_of_visit"][0], "Date cannot be in the past"
        )
