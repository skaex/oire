import factory
from ..models import QuestionSet, Evaluation, Key, Category, Question
from sections.tests.factories import SemesterFactory, SectionFactory


class QuestionSetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuestionSet

    name = factory.Sequence(lambda n: 'questionset-{0}'.format(n))


class EvaluationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evaluation

    name = factory.Sequence(lambda n: 'evaluation-{0}'.format(n))
    semester = factory.SubFactory(SemesterFactory)
    question_set = factory.SubFactory(QuestionSetFactory)


class KeyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Key

    value = factory.Sequence(lambda n: 'key-{0}'.format(n))
    section = factory.SubFactory(SectionFactory)
    evaluation = factory.SubFactory(EvaluationFactory)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category-{0}'.format(n))
    question_set = factory.SubFactory(QuestionSetFactory)


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    category = factory.SubFactory(CategoryFactory)
    title = factory.Sequence(lambda n: 'title-{0}'.format(n))
    description = factory.Sequence(lambda n: 'description-{0}'.format(n))
