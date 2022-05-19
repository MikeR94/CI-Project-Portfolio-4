from django.urls import reverse, resolve
from django.test import TestCase
from Accounts.models import User
from Booking.models import Booking
from Reviews.models import Review
from Staff.models import Payment
from Staff.views import staff_all_bookings, staff_all_reviews, staff_approve_booking, staff_approve_review, staff_cancel_booking, staff_check_in, staff_check_in_page, staff_create_payment, staff_dashboard, staff_deny_booking, staff_deny_review, staff_details_booking, staff_no_show, staff_payment_page, staff_pending_bookings, staff_pending_reviews

class TestUrls(TestCase):

    def test_staff_dashboard_url_is_resolved(self):
        response = self.client.get('/staff/dashboard')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/dashboard')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_dashboard')
        self.assertEquals(resolve(url).func, staff_dashboard)
        self.assertTemplateUsed(response, 'staff_dashboard.html')


    def test_staff_pending_bookings_url_is_resolved(self):
        response = self.client.get('/staff/pending-bookings')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/pending-bookings')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_pending_bookings')
        self.assertEquals(resolve(url).func, staff_pending_bookings)
        self.assertTemplateUsed(response, 'staff_pending_bookings.html')


    def test_staff_approve_bookings_url_is_resolved(self):

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        response = self.client.get('/staff/approve-booking/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_approve_booking', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_approve_booking)
        

    def test_staff_deny_bookings_url_is_resolved(self):

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        response = self.client.get('/staff/deny-booking/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_deny_booking', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_deny_booking)

    
    def test_staff_pending_reviews_url_is_resolved(self):
        response = self.client.get('/staff/pending-reviews')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/pending-reviews')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_pending_reviews')
        self.assertEquals(resolve(url).func, staff_pending_reviews)
        self.assertTemplateUsed(response, 'staff_pending_reviews.html')

    

    def test_staff_approve_review_url_is_resolved(self):

        self.user = User.objects.create_user(username='admin', is_staff=True, id="50")
        self.client.force_login(self.user)

        Review.objects.create(
            id = "50",
            user_id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            body = "hello",
        )

        response = self.client.get('/staff/approve-booking/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_approve_review', kwargs={'review_id': '50'})
        self.assertEquals(resolve(url).func, staff_approve_review)


    def test_staff_deny_review_url_is_resolved(self):

        self.user = User.objects.create_user(username='admin', is_staff=True, id="50")
        self.client.force_login(self.user)

        Review.objects.create(
            id = "50",
            user_id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            body = "hello",
        )

        response = self.client.get('/staff/deny-booking/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_deny_review', kwargs={'review_id': '50'})
        self.assertEquals(resolve(url).func, staff_deny_review)


    def test_staff_details_bookings_url_is_resolved(self):

        response = self.client.get('/staff/details-booking/50')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        response = self.client.get('/staff/details-booking/50')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_details_booking', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_details_booking)
        self.assertTemplateUsed(response, 'staff_details_booking.html')


    def test_staff_all_bookings_url_is_resolved(self):

        response = self.client.get('/staff/all-bookings')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/all-bookings')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_all_bookings')
        self.assertEquals(resolve(url).func, staff_all_bookings)


    def test_staff_all_reviews_url_is_resolved(self):

        response = self.client.get('/staff/all-reviews')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/all-reviews')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_all_reviews')
        self.assertEquals(resolve(url).func, staff_all_reviews)
        self.assertTemplateUsed(response, 'staff_all_reviews.html')


    def test_staff_check_in_page_url_is_resolved(self):

        response = self.client.get('/staff/check-in-page')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/check-in-page')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_check_in_page')
        self.assertEquals(resolve(url).func, staff_check_in_page)
        self.assertTemplateUsed(response, 'staff_check_in.html')


    def test_staff_check_in_booking_id_url_is_resolved(self):

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/check-in/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_check_in', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_check_in)


    def test_staff_no_show_booking_id_url_is_resolved(self):

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/no-show/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_no_show', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_no_show)


    def test_staff_payment_page_url_is_resolved(self):

        response = self.client.get('/staff/payment-page')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/payment-page')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_payment_page')
        self.assertEquals(resolve(url).func, staff_payment_page)
        self.assertTemplateUsed(response, 'staff_payment_page.html')


    def test_staff_create_payment_url_is_resolved(self):

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        response = self.client.get('/staff/create-payment/50')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/create-payment/50')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_create_payment', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_create_payment)
        self.assertTemplateUsed(response, 'staff_submit_payment.html')


    def test_staff_details_booking_cancel_booking_url_is_resolved(self):

        Booking.objects.create(
            id = "50",
            first_name = "Mike",
            last_name = "Ralph",
            email = "testemail@hotmail.co.uk",
            ref_number = "1234567890",
            date_of_visit = "2022-05-16",
            time_of_visit = "20:00:00",
            number_of_guests = "4",
            contact_number = "07436123635"
        )

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/details-booking/cancel/50')
        self.assertEqual(response.status_code, 302)

        url = reverse('staff_cancel_booking', kwargs={'booking_id': '50'})
        self.assertEquals(resolve(url).func, staff_cancel_booking)


class TestModels(TestCase):

    def test_payment_model(self):
        """
        Testing payment model is accepting correct values
        """
        
        payment = Payment.objects.create(
            id = 1,
            amount_owed = 200,
            amount_paid = 220,
            amount_tipped = 20,
            total_income = 220,
        )

        self.assertEquals(payment.id, 1)
        self.assertEquals(payment.amount_owed, 200)
        self.assertEquals(payment.amount_paid, 220)
        self.assertEquals(payment.amount_tipped, 20)
        self.assertEquals(payment.total_income, 220)



