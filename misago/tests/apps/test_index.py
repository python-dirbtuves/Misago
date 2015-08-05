from django_webtest import WebTest

from misago.utils.testing import load_fixtures


class IndexPageTests(WebTest):

    def test_index(self):
        load_fixtures()
        resp = self.app.get('/')
        self.assertEqual(resp.status_int, 200)
