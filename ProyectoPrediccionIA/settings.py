import os
from pathlib import Path

DEBUG = True #False para producción

ALLOWED_HOSTS = []

#En producción con DEBUG = False: 
#ALLOWED_HOSTS = ['127.0.0.1','nombre_dominio','ip_específica','0.0.0.0']
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'proyect'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appServicioPrediccion.apps.AppservicioprediccionConfig',#Se incluye la app
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    #'DEFAULT_AUTHENTICATION_CLASSES': [
    #    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# CORS Config
CORS_ORIGIN_ALLOW_ALL = True

#https://www.django-rest-framework.org/api-guide/parsers/
#https://www.geeksforgeeks.org/how-to-enable-cors-headers-in-your-django-project/
#CORS_ORIGIN_ALLOW_ALL = False
#CORS_ORIGIN_WHITELIST = (
#  'http://localhost:8000',
#)

ROOT_URLCONF = 'ProyectoPrediccionIA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['appServicioPrediccion/Template'], #Se indica el directorio de Templates
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

WSGI_APPLICATION = 'ProyectoPrediccionIA.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'