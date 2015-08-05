import factory
import factory.django


class FullAccessForumRole(factory.django.DjangoModelFactory):
    name = 'Full Access'

    class Meta:
        model = 'misago.ForumRole'
        django_get_or_create = ('name',)


class ReadOnlyForumRole(factory.django.DjangoModelFactory):
    name = "Read only"

    class Meta:
        model = 'misago.ForumRole'
        django_get_or_create = ('name',)
