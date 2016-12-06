from ..forms import SchoolForm, CourseForm
from .factories import SchoolFactory, CourseFactory
from accounts.tests.test_views import AuthViewTest


class SchoolViewTest(AuthViewTest):
    def setUp(self):
        self.school_factory = SchoolFactory
        super(SchoolViewTest, self).setUp()

    def test_list_schools_renders_right_template(self):
        response = self.client.get('/courses/schools/')
        self.assertTemplateUsed(response, 'courses/management/school/list.html')

    def test_add_schools_uses_right_form(self):
        response = self.client.get('/courses/schools/new/')
        self.assertIsInstance(response.context['form'], SchoolForm)

    def test_edit_school_uses_right_form(self):
        new_school = self.school_factory.create()
        response = self.client.get('/courses/schools/%d/edit/' % (new_school.id))
        self.assertIsInstance(response.context['form'], SchoolForm)

    def test_edit_school_uses_right_template(self):
        new_school = self.school_factory.create()
        response = self.client.get('/courses/schools/%d/edit/' % (new_school.id))
        self.assertTemplateUsed(response, 'courses/management/school/form.html')

    # There might be need to test the object returned in the form

    def test_delete_school_uses_right_template(self):
        new_school = self.school_factory.create()
        response = self.client.get('/courses/schools/%d/delete/' % (new_school.id))
        self.assertTemplateUsed(response, 'courses/management/school/delete.html')


class CourseViewTest(AuthViewTest):
    def setUp(self):
        self.course_factory = CourseFactory
        super(CourseViewTest, self).setUp()

    def test_list_courses_renders_right_template(self):
        response = self.client.get('/courses/courses/')
        self.assertTemplateUsed(response, 'courses/management/course/list.html')

    def test_add_course_uses_right_form(self):
        response = self.client.get('/courses/courses/new/')
        self.assertIsInstance(response.context['form'], CourseForm)

    def test_edit_course_uses_right_form(self):
        new_course = self.course_factory.create()
        response = self.client.get('/courses/courses/%d/edit/' % (new_course.id))
        self.assertIsInstance(response.context['form'], CourseForm)

    def test_delete_course_uses_right_template(self):
        new_course = self.course_factory.create()
        response = self.client.get('/courses/courses/%d/delete/' % (new_course.id))
        self.assertTemplateUsed(response, 'courses/management/course/delete.html')






