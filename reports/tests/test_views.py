from django.test import TestCase


class ReportsPageViewTest(TestCase):
    def test_list_reports_renders_right_template(self):
        response = self.client.get('/reports/')
        self.assertTemplateUsed(response, 'reports/report/list.html')


class CreditsViewTest(TestCase):
    def test_show_credits_renders_right_template(self):
        response = self.client.get('/reports/credits/')
        self.assertTemplateUsed(response, 'reports/display/credits.html')
