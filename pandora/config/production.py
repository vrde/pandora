from pandora.config.base import *


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pandora',
        'USER': 'pandora',
        'PASSWORD': 'pandora',
        'HOST': 'localhost',
    }
}

UPLOAD_PATH = '/webapps/pandora/uploads'

