# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys

CURRENT_RELEASE = "0.0"

CWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get("DEBUG", "True").lower() == 'true'
DOCKER = os.environ.get("DOCKER", "False").lower() == 'true'
CACHING = True
CACHE_PAGES = CACHING and not DEBUG
SSL_ENABLED = False

if CACHING:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211' if DOCKER else '127.0.0.1:11211',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


# Tests if tests are running --------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
TESTING = 'test' in sys.argv

# Application production settings ----------------------------------------------
WSGI_APPLICATION = 'main.wsgi.application'
SECRET_KEY = 'd7g65ytreERTDYFUGHIJO8U97653f6ty8ed6hihihi'
APP_NAME = "{{name}}"
STATIC_DOMAIN = "{{staticdomainname}}"
DOMAIN = "{{domainname}}"
SITE_URL = ("https://" if SSL_ENABLED else "http://") + DOMAIN
ALLOWED_HOSTS = ["." + DOMAIN, 'localhost', '127.0.0.1'] if not DEBUG else ["*"]
INTERNAL_IPS = ('127.0.0.1',)

# Default loggers -------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'debug-file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(CWD, 'logs', 'debug.log'),
            'filters': ['require_debug_true']
        },
        'error-file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(CWD, 'logs', 'error.log'),
            'filters': ['require_debug_false']
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'simple',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'error-file', 'debug-file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['error-file'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

# People receiving logs ........................
ADMINS = (
    ('philip', 'philip.garnero@gmail.com'),
)
MANAGERS = ADMINS

# Email settings --------------------------------------------------------------
DEFAULT_TO_EMAIL = MANAGERS
DEFAULT_FROM_EMAIL = '"Django" <django@{{domainname}}>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    if DOCKER:
        EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
    EMAIL_USE_SSL = True
    EMAIL_PORT = 465
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''

# Time and date settings ------------------------------------------------------
TIME_ZONE = 'Europe/Paris'
USE_TZ = False
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i'

# Default file config from Django ---------------------------------------------
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                'django.template.context_processors.request',
                "django.contrib.messages.context_processors.messages",
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ]
        },
    },
]

# Post processing of requests -------------------------------------------------
if CACHE_PAGES:
    MIDDLEWARE = (
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    )
else:
    MIDDLEWARE = ()

MIDDLEWARE += (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
)

# Sessions manager ------------------------------------------------------------
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_AGE = 604800
SESSION_COOKIE_SECURE = SSL_ENABLED
CSRF_COOKIE_SECURE = SSL_ENABLED

# Messages config --------------------------------------------------------------
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.WARNING: 'warning',
    messages.SUCCESS: 'success',
    messages.ERROR: 'alert',
}

# Site database ---------------------------------------------------------------
if not DOCKER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['MYSQL_DATABASE'],
            'USER': os.environ['MYSQL_USER'],
            'PASSWORD': os.environ['MYSQL_PASSWORD'],
            'HOST': 'db',
            'PORT': '3306',
        }
    }

# File options ----------------------------------------------------------------
STATICFILES_DIRS = (os.path.join(CWD, 'front', 'build'),
                    os.path.join(CWD, 'static'),)
STATIC_URL = "/static/"
if not DEBUG:
    STATIC_URL = ("https://" if SSL_ENABLED else "http://") + STATIC_DOMAIN + "/"
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_ROOT = os.path.join(CWD, 'public')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(CWD, 'main', 'media', 'public')
PROTECTED_URL = '/protected-media/'
PROTECTED_ROOT = os.path.join(CWD, 'main', 'media', 'protected')
ROOT_URLCONF = 'main.urls'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Applications in use by the site ---------------------------------------------
PROJECT_APPS = (
    'main',
    'main.apps.app',
)
INSTALLED_APPS = (
    'admin_interface',
    'flat_responsive',
    'colorfield',
    'smuggler',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'annoying',
    'corsheaders',
    'django_extensions',
    'django_filters',
    'djcelery_email',
    'gunicorn',
    'multiselectfield',
    'mail_templated',
    'oauth2_provider',
    'rest_framework',
    'rest_framework_social_oauth2',
    'social_django',
) + PROJECT_APPS

# Cors headers .................................
from corsheaders.defaults import default_headers
CORS_ORIGIN_ALLOW_ALL = DEBUG
CORS_ORIGIN_WHITELIST = (
    STATIC_DOMAIN,
    'localhost:3000',
    '127.0.0.1:3000'
)
CORS_URLS_REGEX = r'^/(api|auth)/.*$'
CORS_ALLOW_HEADERS = default_headers + (
    'cache-control',
)

# Celery .......................................
from celery.schedules import crontab
from datetime import timedelta
if not DOCKER:
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
else:
    CELERY_BROKER_URL = 'redis://redis:6379/0'

CELERY_BEAT_SCHEDULE = {
#    'example': {
#        'task': 'main.apps.app.tasks.example',
#        'schedule': crontab(hour=8, minute=30),
#        'args': ()
#    }
}

# Rest Framework ...............................
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    ),
}

# Python social auth ...........................
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = LOGIN_URL

AUTH_USER_MODEL = "auth.User"
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

AUTHENTICATION_BACKENDS = (
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
RAISE_EXCEPTIONS = DEBUG

# AWS S3 .......................................
AWS_ACCESS_KEY_ID = 'AKIAJHGX5IZ7UHHEGJJQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = STATIC_DOMAIN
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
AWS_S3_SECURE_URLS = False
