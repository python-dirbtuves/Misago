from django.core.management import call_command

from django_webtest import WebTest


class IndexPageTests(WebTest):

    def test_index(self):
        call_command('syncfixtures', quiet=1)
        resp = self.app.get('/')
        self.assertEqual(resp.status_int, 200)
