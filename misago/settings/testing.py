from misago.settings.development import *

SECRET_KEY = 'SECRET4TESTS'

CACHES['default'] = {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
}

SKIP_SOUTH_TESTS = True

MEDIA_URL = "http://media.domain.com/"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
