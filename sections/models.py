from django.db import models
from accounts.models import User
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=15,
                              choices=STATUSES,
                              default=STATUSES[1][0])
    instructors = models.ManyToManyField(
        User)
    enrolled = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.crn


class PreSection(models.Model):
    crn = models.CharField(max_length=20, blank=True)
    course = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    instructors = models.TextField(blank=True)
    enrolled = models.CharField(max_length=10, blank=True)
    semester = models.CharField(max_length=50, blank=True)
    error_column = models.CharField(max_length=50, blank=True)
    error_message = models.TextField(blank=True)

    def save(self, *args, **kwargs):

        fs = [f.name for f in self._meta.get_fields()]

        # This was awesome
        for fie in fs:
            if fie == 'error_column' or fie == 'error_message':
                continue
            if getattr(self, fie) == '':
                self.error_column = fie
                self.error_message = fie + ' cannot be empty'
                break
        else:
            self.error_message = ''
            self.error_column = ''

        if self.error_column == '':
            if not Course.objects.filter(code=self.course).first():
                self.error_column = 'course'
                self.error_message = 'This course is not in our records'
            smstr = self.semester.split(' ')
            if not Semester.objects.filter(season=smstr[0], year=smstr[1]).first():
                self.error_column = 'semester'
                self.error_message = 'This semester is not in our records'

            instrs = self.instructors.split(', ')
            for instr in instrs:
                if not User.objects.filter(email=instr):
                    self.error_column = 'instructors'
                    self.error_message = instr + ' is not in our records'
                    break
        super(PreSection, self).save(*args, **kwargs)

    def __str__(self):
        return 'PRE-SECTION-%s' %(self.crn)
