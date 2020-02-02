"""
Django settings for waterwatch project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '00mf#-^xai5%!%0y5^n(sl1ao1n9bd4)a-1lr_74=rtib5d05o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['35.233.142.155', 'localhost', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'djgeojson',
    'waterwatchapp',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'waterwatch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'waterwatch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'cptwater',
         'USER': 'waterwatch',
         'PASSWORD': 'postgres',
         'HOST': 'localhost',
    }
}

SERIALIZATION_MODULES = {
    'geojson':'djgeojson.serializers'
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = BASE_DIR + '/waterwatchapp/static/'

STATIC_ROOT = BASE_DIR + '/waterwatchapp/static'
# posixpath.join(*(BASE_DIR.split(os.path.sep)
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (33.346444, 103.459442),
    'DEFAULT_ZOOM': 3,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 2,
    'SCALE':'both',
    'ATTRIBUTION_PREFIX':'&copy; <a href="http://strategyrule.com" target="_blank">STRATEGYRULE.COM</a>',
    'TILES': [('Data Map', 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', {'attribution':'&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions" target="_blank">CartoDB</a>', 'maxZoom': 20}),
          #   ('Open Street Map', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>', 'maxZoom': 20}),
          # ('Terrain Map', 'http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community', 'maxZoom': 20})
          ],
    # 'OVERLAYS': [('Suburbs', 'https://citymaps.capetown.gov.za/agsext1/rest/services/Theme_Based/EGISViewer/MapServer/76/query?outFields=*&where=1%3D1', {'attribution': '&copy; IGN'}),
    #              ('Dams', 'http://server/a/{z}/{x}/{y}.png', {'attribution': '&copy; IGN'})]

}
