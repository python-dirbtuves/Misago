import factory
import factory.django


class RootForum(factory.django.DjangoModelFactory):
    special = 'root'
    name = 'root'
    slug = 'root'

    class Meta:
        model = 'misago.Forum'
        django_get_or_create = ('slug',)


class CategoryForum(factory.django.DjangoModelFactory):
    type = 'category'
    slug = 'first-category'
    name = 'First Category'
    parent = factory.SubFactory(RootForum)

    class Meta:
        model = 'misago.Forum'
        django_get_or_create = ('slug',)


class RedirectForum(factory.django.DjangoModelFactory):
    type = 'redirect'
    slug = 'project-homepage'
    name = 'Project Homepage'
    redirect = 'http://misago-project.org'

    class Meta:
        model = 'misago.Forum'
        django_get_or_create = ('slug',)


class ForumFactory(factory.django.DjangoModelFactory):
    type = 'forum'
    slug = 'first-forum'
    name = 'First Forum'
    parent = factory.SubFactory(CategoryForum)

    class Meta:
        model = 'misago.Forum'
        django_get_or_create = ('slug',)
