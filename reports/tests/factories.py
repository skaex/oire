import factory
from sections.tests.factories import SectionFactory
from evaluations.tests.factories import EvaluationFactory, QuestionFactory
from ..models import Response, Comment


class ResponseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Response

    section = factory.SubFactory(SectionFactory)
    evaluation = factory.SubFactory(EvaluationFactory)
    question = factory.SubFactory(QuestionFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    comment = factory.Sequence(lambda n: 'comment-{0}'.format(n))
    section = factory.SubFactory(SectionFactory)
    evaluation = factory.SubFactory(EvaluationFactory)

