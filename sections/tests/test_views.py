from ..forms import SemesterForm, SectionForm
from .factories import SemesterFactory, SectionFactory
from accounts.tests.test_views import AuthViewTest


class SemesterViewTest(AuthViewTest):
    def setUp(self):
        self.factory = SemesterFactory
        super(SemesterViewTest, self).setUp()

    def test_list_semesters_renders_right_template(self):
        response = self.client.get('/sections/semesters/')
        self.assertTemplateUsed(response, 'sections/management/semester/list.html')

    def test_add_semesters_uses_right_form(self):
        response = self.client.get('/sections/semesters/new/')
        self.assertIsInstance(response.context['form'], SemesterForm)

    def test_edit_school_uses_right_form(self):
        new_semester = self.factory.create()
        response = self.client.get('/sections/semesters/%d/edit/' % (new_semester.id))
        self.assertIsInstance(response.context['form'], SemesterForm)

    # This also the same suggestion as in above
    #
    def test_delete_school_uses_right_template(self):
        new_semester = self.factory.create()
        response = self.client.get('/sections/semesters/%d/delete/' % (new_semester.id))
        self.assertTemplateUsed(response, 'sections/management/semester/delete.html')


class SectionViewTest(AuthViewTest):
    def setUp(self):
        self.factory = SectionFactory
        super(SectionViewTest, self).setUp()

    def test_list_sections_renders_right_template(self):
        response = self.client.get('/sections/sections/')
        self.assertTemplateUsed(response, 'sections/management/section/list.html')

    def test_add_sections_uses_right_form(self):
        response = self.client.get('/sections/sections/new/')
        self.assertIsInstance(response.context['form'], SectionForm)

    def test_edit_view_uses_right_form(self):
        new_section = self.factory.create()
        response = self.client.get('/sections/sections/%d/edit/' % (new_section.id))
        self.assertIsInstance(response.context['form'], SectionForm)

    def test_delete_view_uses_right_template(self):
        new_section = self.factory.create()
        response = self.client.get('/sections/sections/%d/delete/' % (new_section.id))
        self.assertTemplateUsed(response, 'sections/management/section/delete.html')
