from django.db import models


class School(models.Model):
    school = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s" % (self.school)


class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    school = models.ForeignKey(School)

    def __str__(self):
        return self.code
