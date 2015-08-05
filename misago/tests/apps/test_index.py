from django_webtest import WebTest

from misago.utils.testing import load_fixtures, login


class IndexPageTests(WebTest):

    def test_index(self):
        load_fixtures()
        resp = self.app.get('/')
        resp.mustcontain("First Forum")

    def test_index_with_authenticated_user(self):
        load_fixtures()
        login(self)

        resp = self.app.get('/')
        resp.mustcontain("Welcome back, registered")
