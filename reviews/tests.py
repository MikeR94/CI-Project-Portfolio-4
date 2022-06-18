from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, resolve
from accounts.models import User
from reviews.forms import ReviewForm
from reviews.models import Review
from reviews.views import create_review


class TestUrls(TestCase):
    """
    A class to test the review URLS
    """
    def test_create_review_url_is_resolved(self):
        """
        Tests if the create_review url is working
        correctly
        """
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
    """
    A class to test the review models
    """
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


class TestForms(TestCase):
    """
    A class to test the review forms
    """
    def test_review_form(self):
        """
        Testing review form is accepting correct values
        """
        self.user = User.objects.create_user(
            username="admin", password="adminadmin", email="admin@example.com"
        )
        self.client.force_login(self.user)

        form = ReviewForm(
            data={
                "first_name": "Mike",
                "last_name": "Ralph",
                "stars": "5 Star",
                "body": """When we think about celebrations, Cafe Manbo
                is always our first option, and it never disappoints.
                From the starter to the dessert the quality and tastes
                of everything was outstanding, my meal might have been
                the best meal I have ever been served. Service was delightful
                and very professional. 10/10.""",
            }
        )
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("stars", form.fields)
        self.assertIn("body", form.fields)

        request = HttpRequest()
        request.POST = {
            "first_name": "Mike",
            "last_name": "Ralph",
            "stars": "5 Star",
            "body": """When we think about celebrations, Cafe Manbo
            is always our first option, and it never disappoints.
            From the starter to the dessert the quality and tastes
            of everything was outstanding, my meal might have been
            the best meal I have ever been served. Service was delightful
            and very professional. 10/10.""",
        }
        test_form = ReviewForm(request.POST)
        self.assertTrue(test_form.is_valid())
