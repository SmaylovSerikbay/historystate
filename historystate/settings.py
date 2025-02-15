import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-your-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Временно включаем для отладки

ALLOWED_HOSTS = [
    'historystate.my-business-card.kz',
    'nginx.my-business-card.kz',
    'localhost',
    '127.0.0.1',
    '77.246.247.179',
    'www.historystate.my-business-card.kz',
    'www.nginx.my-business-card.kz',
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
    'ckeditor',
    'ckeditor_uploader',
    'main',
    'blog',
    'gallery',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'historystate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'historystate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'historystate',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CKEditor settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

# Admin interface customization
JAZZMIN_SETTINGS = {
    "site_title": "History State Admin",
    "site_header": "History State",
    "site_brand": "History State",
    "welcome_sign": "Welcome to History State Admin",
    "copyright": "History State",
    "search_model": ["auth.User", "main.News", "main.Event", "main.ResearchProject"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Site", "url": "/", "new_window": True},
    ],
    "icons": {
        "main.Hero": "fas fa-home",
        "main.Event": "fas fa-calendar-alt",
        "main.Banner": "fas fa-image",
        "main.News": "fas fa-newspaper",
        "main.Resource": "fas fa-book",
        "main.ResearchProject": "fas fa-project-diagram",
        "main.Recommendation": "fas fa-thumbs-up",
        "main.Journal": "fas fa-journal-whills",
        "main.ExpertOpinion": "fas fa-user-graduate",
        "main.Achievement": "fas fa-trophy",
    },
}

# Translation settings
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'main', 'locale'),
]

LANGUAGES = [
    ('ru', 'Russian'),
    ('kk', 'Kazakh'),
    ('en', 'English'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('ru', 'kk', 'en')}

# Настройки для работы через прокси
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PROTO = True
CSRF_TRUSTED_ORIGINS = ['http://historystate.my-business-card.kz', 'https://historystate.my-business-card.kz', 'http://nginx.my-business-card.kz', 'https://nginx.my-business-card.kz']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False  # Временно отключаем
SESSION_COOKIE_SECURE = False  # Временно отключаем
CSRF_COOKIE_SECURE = False  # Временно отключаем
SECURE_HSTS_SECONDS = 0  # Временно отключаем
SECURE_HSTS_INCLUDE_SUBDOMAINS = False  # Временно отключаем
SECURE_HSTS_PRELOAD = False  # Временно отключаем
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Дополнительные настройки безопасности
SECURE_REFERRER_POLICY = 'same-origin'
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax' 