from django_webtest import WebTest


class IndexPageTests(WebTest):

    def test_index(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_int, 200)
