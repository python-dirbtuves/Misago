from django.core.management import call_command

from django_webtest import WebTest

from misago.factories.forummodel import ForumFactory


class ForumListTests(WebTest):

    def test_forum_list_annonymous(self):
        call_command('syncfixtures', quiet=1)

        forum = ForumFactory()

        resp = self.app.get('/forum/%s-%d/' % (forum.slug, forum.pk))
        resp.mustcontain('First Forum')
