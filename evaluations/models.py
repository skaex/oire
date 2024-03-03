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
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Key(models.Model):
    HELPER_KEY_LENGTH = 6
    KEY_LENGTH = 5
    KEY_STATUSES = (
        ('FRESH', 'Fresh'),
        ('GIVEN_OUT', 'Given out'),
        ('USED', 'Used'),
    )
    value = models.CharField(max_length=10, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=KEY_STATUSES, default=KEY_STATUSES[0][0])
    helper = models.BooleanField(default=False)

    def __str__(self):
        return self.value


class Category(models.Model):
    name = models.CharField(max_length=50)
    question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' %(self.name, self.question_set.name)

    class Meta:
        unique_together = ('name', 'question_set')


class Question(models.Model):
    category = models.ForeignKey(Category, related_name='category_questions', on_delete=models.CASCADE)
    order = OrderField(blank=True, for_fields=['category'])
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return '(%s) %s: %s' %(self.category, self.title, self.description)