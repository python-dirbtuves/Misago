import factory
import factory.django


class ForumFactory(factory.django.DjangoModelFactory):
    slug = 'first-forum'

    class Meta:
        model = 'misago.Forum'
        django_get_or_create = ('slug',)
