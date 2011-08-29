# coding: utf-8

from config import INTERNAL_IPS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Odchytavat static files
MANAGING_STATIC_FILES = True

# Pokud chceme povolit www v adrese.
PREPEND_WWW = False

INTERNAL_IPS += ()

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        }
    }
}

###################
## Odesilani emailu

## Pokud se pouzije filebesed backed dojde k odeslani mailu ktery se zapise pouze do EMAIL_FILE_PATH
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'

## Odesilani emailu pres SMTP
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.kk.cz'
#EMAIL_HOST_USER = 'info@kk.cz'
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True
#EMAIL_SUBJECT_PREFIX = U'[kk]'

