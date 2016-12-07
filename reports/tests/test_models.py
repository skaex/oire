from django.test import TestCase
from .factories import ResponseFactory, CommentFactory
from ..models import Response, Comment


class ResponseModelTest(TestCase):
    def setUp(self):
        self.factory = ResponseFactory

    def test_can_create_response(self):
        response = self.factory.create()
        self.assertEqual(list(Response.objects.all()), [response, ])

    def test_string_representation(self):
        response = self.factory.build()
        self.assertEqual(str(response), str([0, 0, 0, 0, 0]))

    def test_default_value_for_scores(self):
        response = self.factory.build()
        self.assertEqual(response.one, 0)
        self.assertEqual(response.two, 0)
        self.assertEqual(response.three, 0)
        self.assertEqual(response.four, 0)
        self.assertEqual(response.five, 0)


class CommentModelTest(TestCase):
    def setUp(self):
        self.factory = CommentFactory

    def test_can_create_comment(self):
        comment = self.factory.create()
        self.assertEqual(list(Comment.objects.all()), [comment])

    def test_string_representation(self):
        comment = self.factory.build()
        self.assertEqual(str(comment), '%s' % (comment.comment))
