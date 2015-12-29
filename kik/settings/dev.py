"""
Django settings for kik project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import imp

pj = os.path.join

def rel(*x):
    return os.path.join(BASE_DIR, *x)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Celery settings

# BROKER_URL = 'amqp://guest:guest@localhost//'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

BASE_DIR = BASE_DIR
TEMP_DIR = rel(BASE_DIR, 'temp_dir')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lke$fdxnd%bo^bei9tkx=nona42*kpv3a4l0h9xc@h=dk-e4n5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
#     'djcelery',
    'rest_framework',
    'kik',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kik.urls'

WSGI_APPLICATION = 'kik.wsgi.dev.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

CACHES = {
    'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': '127.0.0.1:11211'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = rel('../..', 'media')
MEDIA_URL = '/media/'

AGENDA_DIR = pj(MEDIA_ROOT, 'agendas')
TEMPLATE_DIR = pj(MEDIA_ROOT, 'templates')

STATIC_URL = '/static/'
STATIC_ROOT = rel('../..', 'static')
STATICFILES_DIRS = (
    rel('static'),
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kik',
#         'TEST_NAME': 'test_kik',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432'
    },
}

PKB_SERVICE_URL = 'http://www-test2.1cb.kz:80/FCBServices/Service?wsdl'
PKB_SERVICE_USERNAME = 'KIKuser09_TST'
PKB_SERVICE_PASSWORD = 'KIKuser09_TST1'

DOCUMENTOLOG_URL = 'http://kik.doc24.kz'
DOCUMENTOLOG_LOGIN_URL = DOCUMENTOLOG_URL + '/user/login'
DOCUMENTOLOG_LOGIN = 'admin@kik.doc24.kz'
DOCUMENTOLOG_PASSWORD = '123456Qw'
DOCUMENTOLOG_MOVE_WSDL = DOCUMENTOLOG_URL + '/ws_kik/workflow/move?wsdl'
DOCUMENTOLOG_EDIT_WSDL = DOCUMENTOLOG_URL + '/ws_kik/workflow/edit?wsdl'
DOCUMENTOLOG_WSDL_USERNAME = 'documentolog'
DOCUMENTOLOG_WSDL_PASSWORD = 'secret'
DOCUMENTOLOG_DOCTYPE_ID = u'f1736069-6e65-41b4-9767-5673ee780073'