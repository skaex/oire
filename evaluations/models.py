from django.db import models
from sections.models import Semester, Section
from .fields import OrderField


class QuestionSet(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    STATUSES = (
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('FINISHED', 'Finished'),
    )
    status = models.CharField(max_length=15,
                              choices=STATUSES,
                              default=STATUSES[1][0])
    name = models.CharField(max_length=250)
    question_set = models.ForeignKey(QuestionSet)
    semester = models.ForeignKey(Semester)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Key(models.Model):
    KEY_STATUSES = (
        ('FRESH', 'Fresh'),
        ('GIVEN_OUT', 'Given out'),
        ('USED', 'Used'),
    )
    value = models.CharField(max_length=10, unique=True)
    section = models.ForeignKey(Section)
    evaluation = models.ForeignKey(Evaluation)
    status = models.CharField(max_length=10, choices=KEY_STATUSES, default=KEY_STATUSES[0][0])
    helper = models.BooleanField(default=False)

    def __str__(self):
        return self.value


class Category(models.Model):
    name = models.CharField(max_length=50)
    question_set = models.ForeignKey(QuestionSet)

    def __str__(self):
        return '%s (%s)' %(self.name, self.question_set.name)

    class Meta:
        unique_together = ('name', 'question_set')


class Question(models.Model):
    category = models.ForeignKey(Category, related_name='category_questions')
    order = OrderField(blank=True, for_fields=['category'])
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return '(%s) %s: %s' %(self.category, self.title, self.description)