from django.db import models
from accounts.models import User
from reviews.utils import validate_not_spaces
from django.core.validators import MinLengthValidator


class Review(models.Model):
    """
    A class to create a Review
    model
    """
    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[validate_not_spaces],
    )
    last_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[validate_not_spaces],
    )
    body = models.TextField(
        editable=True,
        blank=False,
        validators=[
            validate_not_spaces,
            MinLengthValidator(
                80, "The field must contain at least 80 characters"),
        ],
    )
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    acknowledged = models.BooleanField(default=False)
    stars = models.CharField(
        max_length=6,
        default="5 Star",
        choices=(
            ("1 Star", "1 star"),
            ("2 Star", "2 star"),
            ("3 Star", "3 star"),
            ("4 Star", "4 star"),
            ("5 Star", "5 star"),
        ),
    )

    def __str__(self):
        """
        Returns the review first name
        """
        return self.first_name
