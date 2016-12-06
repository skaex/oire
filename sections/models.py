from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Semester(models.Model):
    season = models.CharField(max_length=10)
    year = models.IntegerField()
    is_current = models.BooleanField(default=False)

    class Meta:
        unique_together = ('season', 'year')

    def __str__(self):
        return "%s %s" % (self.season, self.year)


class Section(models.Model):
    STATUSES = (
        ('OPEN', 'Open'),
        ('LOCKED', 'Locked'),
        ('IN_PROGRESS', 'In progress'),
        ('DONE', 'Done'),
    )
    crn = models.CharField(max_length=20)
    course = models.ForeignKey(Course)
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=15,
                              choices=STATUSES,
                              default=STATUSES[1][0])
    instructors = models.ManyToManyField(
        User)
    enrolled = models.IntegerField()
    semester = models.ForeignKey(Semester)

    def __str__(self):
        return self.crn
