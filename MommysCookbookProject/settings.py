import os
from pathlib import Path

from django.urls import reverse_lazy


BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@x5om%n=@%alzx8mhm5zzawy75y-(m5a9@c8&=wb+8gj7uib@("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django.contrib.humanize",

    # Project Apps
    "MommysCookbookProject.home",
    "MommysCookbookProject.recipe",
    "MommysCookbookProject.user_auth",


]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "MommysCookbookProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "MommysCookbookProject.wsgi.application"



DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'mommys_cookbook_db',
    'USER': 'postgres-dd',
    'PASSWORD': '1234',
    'HOST': '127.0.0.1',
    'PORT': '5432'
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True




STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'static']


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_URL = reverse_lazy("user_login")
LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGOUT_REDIRECT_URL = reverse_lazy("user_login")


AUTH_USER_MODEL = 'user_auth.CookbookUser'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

