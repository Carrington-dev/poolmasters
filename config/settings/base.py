import os
from pathlib import Path
from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'ftUpUlNEc3CeBJ5mo6k7tViiEH4JRPLVXheEhRuG4eiRWkwx9Zsiyw4Vel4xY2ix'

DEBUG = True

ALLOWED_HOSTS = ['*']
APPS_DIR = BASE_DIR / "vroomtradex"


THIRD_PARTY = [
    'grappelli',
]

DEFAULT_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'applications.users',
    'applications.book',
]

INSTALLED_APPS = THIRD_PARTY + DEFAULT_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./applications/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                "applications.users.context_processors.important"
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'applications/files/logs/db.sqlite3',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "applications/files/media")
STATIC_ROOT = os.path.join(BASE_DIR, "applications/files/static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'applications/files/assets'),
]

MESSAGE_TAGS = {
    messages.DEBUG : 'alert-info',
    messages.INFO : 'alert-info',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
    messages.ERROR : 'alert-danger',
    # messages.ERROR: 'danger',
}

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
DEFAULT_FROM_ADMIN = os.environ.get('DEFAULT_FROM_ADMIN')



DEFAULT_FROM_EMAIL = 'Carrington Visionary Academy <support@mail.cvacademy.co.za>'
