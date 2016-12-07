from ..forms import QuestionSetForm, EvaluationForm, CategoryForm, QuestionForm, EvaluateForm
from .factories import QuestionSetFactory, EvaluationFactory, QuestionFactory, CategoryFactory, KeyFactory
from accounts.tests.test_views import AuthViewTest


class QuestionSetViewTest(AuthViewTest):
    def setUp(self):
        self.factory = QuestionSetFactory
        super(QuestionSetViewTest, self).setUp()

    def test_list_questionset_view_renders_right_template(self):
        response = self.client.get('/evaluations/questionsets/')
        self.assertTemplateUsed(response, 'evaluations/management/questionset/list.html')

    def test_add_questionset_view_uses_right_form(self):
        response = self.client.get('/evaluations/questionsets/new/')
        self.assertIsInstance(response.context['form'], QuestionSetForm)

    def test_edit_questionset_uses_right_form(self):
        new_questionset = self.factory.create()
        response = self.client.get('/evaluations/questionsets/%d/edit/' % (new_questionset.id))
        self.assertIsInstance(response.context['form'], QuestionSetForm)


class EvaluationViewTest(AuthViewTest):
    def setUp(self):
        self.factory = EvaluationFactory
        super(EvaluationViewTest, self).setUp()

    def test_list_evaluation_view_renders_right_template(self):
        response = self.client.get('/evaluations/evaluations/')
        self.assertTemplateUsed(response, 'evaluations/management/evaluation/list.html')

    def test_add_evaluation_view_uses_right_form(self):
        response = self.client.get('/evaluations/evaluations/new/')
        self.assertIsInstance(response.context['form'], EvaluationForm)

    def test_edit_evaluation_uses_right_form(self):
        new_evaluation = self.factory.create()
        response = self.client.get('/evaluations/evaluations/%d/edit/' % (new_evaluation.id))
        self.assertIsInstance(response.context['form'], EvaluationForm)

    # This is probably a functional test
    # def test_open_evaluation_view_open_the_right_evaluation(self):
    # 	new_evaluation = self.factory.create()
    # 	# I wouldn't check if the default status because there is a test for that
    # 	self.client.get('/evaluations/evaluation/open/%d/' %(new_evaluation.id))
    # 	print(new_evaluation.status)
    # 	self.assertEqual(new_evaluation.status, Evaluation.STATUSES[0][0])


class CategoryEvaluation(AuthViewTest):
    def setUp(self):
        self.factory = CategoryFactory
        super(CategoryEvaluation, self).setUp()

    def test_add_category_view_renders_right_template(self):
        response = self.client.get('/evaluations/categories/new/')
        self.assertIsInstance(response.context['form'], CategoryForm)

    def test_edit_category_uses_right_form(self):
        new_category = self.factory.create()
        response = self.client.get('/evaluations/categories/%d/edit/' % (new_category.id))
        self.assertIsInstance(response.context['form'], CategoryForm)


class QuestionViewTest(AuthViewTest):
    def setUp(self):
        self.factory = QuestionFactory
        super(QuestionViewTest, self).setUp()

    def test_list_questions_view_renders_right_template(self):
        response = self.client.get('/evaluations/questions/')
        self.assertTemplateUsed(response, 'evaluations/management/question/list.html')

    def test_add_question_view_uses_right_form(self):
        response = self.client.get('/evaluations/questions/new/')
        self.assertIsInstance(response.context['form'], QuestionForm)

    def test_edit_question_view_uses_right_form(self):
        new_question = self.factory.create()
        response = self.client.get('/evaluations/questions/%d/edit/' % (new_question.id))
        self.assertIsInstance(response.context['form'], QuestionForm)


class KeyViewTest(AuthViewTest):
    def setUp(self):
        self.factory = KeyFactory
        super(KeyViewTest, self).setUp()

    def test_list_key_by_section_renders_right_template(self):
        new_key = self.factory.create()
        response = self.client.get('/evaluations/keys/section/%d/' % (new_key.section.id))
        self.assertTemplateUsed(response, 'evaluations/management/key/list.html')


class EvaluateFormViewTest(AuthViewTest):
    def test_get_evaluate_form_view_renders_right_form(self):
        response = self.client.get('/evaluations/evaluate/')
        self.assertIsInstance(response.context['form'], EvaluateForm)

    def test_get_evaluate_form_view_renders_right_template(self):
        response = self.client.get('/evaluations/evaluate/form.html')
        self.assertTemplateUsed('evaluation')
