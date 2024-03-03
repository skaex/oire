from django.db import models
from evaluations.models import Evaluation, Question
from sections.models import Section


class Response(models.Model):
    one = models.IntegerField(default=0)
    two = models.IntegerField(default=0)
    three = models.IntegerField(default=0)
    four = models.IntegerField(default=0)
    five = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str([self.one, self.two, self.three, self.four, self.five])


class Comment(models.Model):
    comment = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
