import factory
import factory.django


class AdministratorRole(factory.django.DjangoModelFactory):
    name = "Administrator"

    class Meta:
        model = 'misago.Role'
        django_get_or_create = ('name',)


class GuestRole(factory.django.DjangoModelFactory):
    name = "Guest"

    class Meta:
        model = 'misago.Role'
        django_get_or_create = ('name',)
