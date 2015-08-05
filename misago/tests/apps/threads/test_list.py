from django_webtest import WebTest

from misago.utils.testing import load_fixtures
from misago.factories.forummodel import ForumFactory


class ForumListTests(WebTest):

    def test_forum_list_annonymous(self):
        load_fixtures()
        forum = ForumFactory()

        resp = self.app.get('/forum/%s-%d/' % (forum.slug, forum.pk))
        resp.mustcontain('First Forum')
