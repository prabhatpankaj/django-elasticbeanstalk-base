import os
import json

# settings
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))

# django 
DJANGO_DIR = os.path.dirname(os.path.dirname(SETTINGS_DIR))

ROOT_DIR = os.path.dirname(DJANGO_DIR)

# django secret key
SECRET_KEY = '(fcu4+@jgr4fvmb+yqk)e+m9x6ux*)kfu^jjf&=($7090o=grk'

DEBUG = True

ALLOWED_HOSTS = []

# User model
AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
]

CUSTOM_APPS = [
    'core',
    'users',
    'pages',
]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware', # corsheaders
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# cors headers
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'config.urls'

# templates
TEMPLATE_DIR = os.path.join(DJANGO_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# media
MEDIA_ROOT = os.path.join(DJANGO_DIR, 'media')
MEDIA_URL = '/temp/'

# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DJANGO_DIR, 'stroot')
STATIC_DIR = os.path.join(DJANGO_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]


# Django Mail Information
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'emailuser'
EMAIL_HOST_PASSWORD = 'emailpassword'
SERVER_EMAIL = 'sample@gmail.com'
DEFAULT_FROM_EMAIL = 'sample@gmail.com'