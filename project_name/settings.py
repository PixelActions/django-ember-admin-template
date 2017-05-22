"""
Django settings for {{project_name}} project.

Generated by 'django-admin startproject' using Django 1.11.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{secret_key}}'

SERVER_TYPE = os.environ.get('SERVER_TYPE', 'Not Set')
# SECURITY WARNING: don't run with debug turned on in production!
if SERVER_TYPE != 'PROD':
    DEBUG = True
else:
    DEBUG = False

if SERVER_TYPE != 'PROD':
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['.pixelactions.com', '.{{project_name}}.com']

# Application definition
INSTALLED_APPS = [
    '{{project_name}}.apps.SuitConfig',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_auto_endpoint',
    'rest_framework',
    'corsheaders',
    'export_app',
    'easy_thumbnails',
    'mptt',
    '{{project_name}}.apps.FilerConfig',
]
if SERVER_TYPE == 'PROD':
    INSTALLED_APPS += ['storages']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{project_name}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = '{{project_name}}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if SERVER_TYPE == 'PROD':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', ''),
        # The following settings are not used with sqlite3:
        'USER': os.environ.get('DB_USERNAME', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

if SERVER_TYPE == 'PROD':
    FORCE_SCRIPT_NAME = "/backend"  # Signifies that this django app is loaded from the sub-url /backend
    STATIC_URL = '/backend/static/'  # % FORCE_SCRIPT_NAME
    WHITENOISE_STATIC_PREFIX = '/static/'
    # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
    # STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
    AWS_AUTO_CREATE_BUCKET = os.environ.get('AWS_AUTO_CREATE_BUCKET', False)
    MEDIA_ROOT = ''
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    MEDIA_URL = "http://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
else:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

EXPORTER_FRONT_APPLICATION_PATH = '../{{project_name}}_ember'
EXPORTER_ROUTER_PATH = '{{project_name}}.urls.router'

CORS_ORIGIN_ALLOW_ALL = True

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_ALIASES = {
    '': {
        'demo_thumb': {'size': (200, 100), 'crop': 'scale', 'background': '#ffffff'},
    },
}

FILER_STORAGES = {
    'public': {
        'main': {
            'OPTIONS': {
                'location': MEDIA_ROOT,
                'base_url': '/media/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'uploads',
        },
        'thumbnails': {
            'OPTIONS': {
                'location': MEDIA_ROOT,
                'base_url': '/media/thumbnails/',
            },
            'THUMBNAIL_OPTIONS': {
                'base_dir': 'thumbnails',
            },
        },
    },
}

APPEND_SLASH = False