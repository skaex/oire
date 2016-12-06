import factory
from ..models import School, Course


class SchoolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = School

    school = factory.Sequence(lambda n: 'school-{0}'.format(n))


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    code = factory.Sequence(lambda n: 'code-{0}'.format(n))
    title = factory.Sequence(lambda n: 'code-{0}'.format(n))
    school = factory.SubFactory(SchoolFactory)
