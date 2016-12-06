import factory
from courses.tests.factories import CourseFactory
from ..models import Semester, Section


class SemesterFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Semester

    season = factory.Sequence(lambda n: 'season-{0}'.format(n))
    year = factory.Faker('year')


class SectionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Section

    crn = factory.Sequence(lambda n: '{0}'.format(n))
    course = factory.SubFactory(CourseFactory)
    time = factory.Sequence(lambda n: 'time-{0}'.format(n))
    location = factory.Sequence(lambda n: 'location-{0}'.format(n))
    enrolled = factory.Sequence(lambda n: '{0}'.format(n))
    semester = factory.SubFactory(SemesterFactory)
