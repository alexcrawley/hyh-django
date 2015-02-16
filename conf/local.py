from conf.default import *


DEBUG = TEMPLATE_DEBUG = True

# Output emails to STDOUT
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location('db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    },
}
