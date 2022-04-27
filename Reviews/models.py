from django.db import models
from Accounts.models import User

# Create your models here.

class Review(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    body = models.TextField(editable=True, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name