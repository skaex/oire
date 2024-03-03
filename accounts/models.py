from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import School


DEFAULT_USER_PASSWORD = "fcevaluation"
TESTING_PASSWORD = 'password'


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]
