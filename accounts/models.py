from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import School


DEFAULT_USER_PASSWORD = "fcevaluation"
TESTING_PASSWORD = 'password'


class User(AbstractUser):
    school = models.ForeignKey(School, null=True)
