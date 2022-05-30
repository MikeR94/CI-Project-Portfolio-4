from django.db import models
from Accounts.models import User
from Reviews.utils import validate_not_spaces

# Create your models here.


class Review(models.Model):
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
        editable=True, blank=False, validators=[validate_not_spaces]
    )
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
