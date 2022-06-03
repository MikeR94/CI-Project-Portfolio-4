from django.test import TestCase
from django.urls import reverse, resolve
from Accounts.models import User
from Reviews.models import Review
from Reviews.views import create_review


class TestUrls(TestCase):
    def test_create_review_url_is_resolved(self):
        response = self.client.get("/create/review")
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)
        response = self.client.get("/create/review")
        self.assertEqual(response.status_code, 200)

        url = reverse("create_review")
        self.assertEquals(resolve(url).func, create_review)
        self.assertTemplateUsed(response, "create_review.html")


class TestModels(TestCase):
    def test_review_model(self):
        """
        Testing review model is accepting correct values
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

        review = Review.objects.create(
            first_name="Mike",
            last_name="Ralph",
            id=1,
            body="Hello",
            approved=True,
            user_id=user.id,
            acknowledged=True,
        )

        self.assertEquals(review.first_name, "Mike")
        self.assertEquals(review.last_name, "Ralph")
        self.assertEquals(review.id, 1)
        self.assertEquals(review.body, "Hello")
        self.assertEquals(review.approved, True)
        self.assertEquals(review.user_id, user.id)
        self.assertEquals(review.acknowledged, True)
