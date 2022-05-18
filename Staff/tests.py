from django.urls import reverse, resolve
from django.test import TestCase
from Accounts.models import User
from Staff.views import staff_dashboard, staff_pending_bookings

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


    def test_staff_pending_bookings_url_is_resolved(self):
        response = self.client.get('/staff/pending-bookings')
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username='admin', is_staff=True)
        self.client.force_login(self.user)

        response = self.client.get('/staff/pending-bookings')
        self.assertEqual(response.status_code, 200)

        url = reverse('staff_pending_bookings')
        self.assertEquals(resolve(url).func, staff_pending_bookings)



