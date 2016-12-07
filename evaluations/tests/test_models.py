from django.core.exceptions import ValidationError
from django.test import TestCase
from .factories import QuestionSetFactory, EvaluationFactory, KeyFactory, QuestionFactory, CategoryFactory
from ..models import QuestionSet, Evaluation, Key, Question, Category


class QuestionSetModelTest(TestCase):
    def setUp(self):
        self.factory = QuestionSetFactory

    def test_can_create_question_set(self):
        question_set = self.factory.create()
        self.assertEqual(list(QuestionSet.objects.all()), [question_set, ])

    def test_string_representation(self):
        question_set = self.factory.create()
        self.assertEqual(str(question_set), question_set.name)

    def test_duplicate_question_set_not_allowed(self):
        question_set_1 = self.factory.create()
        with self.assertRaises(ValidationError):
            question_set = QuestionSet(name=question_set_1.name)
            question_set.full_clean()


class EvaluationModelTest(TestCase):
    def setUp(self):
        self.factory = EvaluationFactory

    # The above line just itches me badly

    def test_can_create_evaluation(self):
        evaluation = self.factory.create()
        self.assertEqual(list(Evaluation.objects.all()), [evaluation, ])

    def test_string_representation(self):
        evaluation = self.factory.create()
        self.assertEqual(str(evaluation), evaluation.name)

    def test_default_status_at_creation(self):
        evaluation = self.factory.create()
        self.assertEqual(evaluation.status, Evaluation.STATUSES[1][0])


class KeyModelTest(TestCase):
    def setUp(self):
        self.factory = KeyFactory

    def test_can_create_key(self):
        key = self.factory.create()
        self.assertEqual(list(Key.objects.all()), [key, ])

    def test_string_representation(self):
        key = self.factory.create()
        self.assertEqual(str(key), key.value)

    def test_duplicate_keys_not_allowed(self):
        key_1 = self.factory.create()
        with self.assertRaises(ValidationError):
            key = Key(value=key_1.value, section=key_1.section, evaluation=key_1.evaluation)
            key.full_clean()

        # Come and test default value


class CategoryModelTest(TestCase):
    def setUp(self):
        self.factory = CategoryFactory

    def test_can_create_category(self):
        category = self.factory.create()
        self.assertEqual(list(Category.objects.all()), [category, ])

    def test_duplicate_category_not_allowed_for_a_question_set(self):
        category_1 = self.factory.create()
        with self.assertRaises(ValidationError):
            category = Category(name=category_1.name, question_set=category_1.question_set)
            category.full_clean()

    def test_string_representation(self):
        category = self.factory.create()
        self.assertEqual(str(category), '%s (%s)' % (category.name, category.question_set.name))


class QuestionModelTest(TestCase):
    def setUp(self):
        self.factory = QuestionFactory

    def test_can_create_question(self):
        question = self.factory.create()
        self.assertEqual(list(Question.objects.all()), [question, ])

    def test_string_representation(self):
        question = self.factory.create()
        self.assertEqual(str(question),
                         '(%s) %s: %s' % (question.category, question.title, question.description))
