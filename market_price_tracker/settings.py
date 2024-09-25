import os
from pathlib import Path
import dj_database_url


PORT =  8000

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'siam1234'

DEBUG = True

ALLOWED_HOSTS = ["bazar-price-tracker-api.onrender.com", '127.0.0.1', 'localhost']


INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bazar',
    'drf_yasg',
    'users',
]


REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
        'anon': '100/day',
    }
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

ROOT_URLCONF = 'market_price_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'market_price_tracker.wsgi.application'



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'market_price_tracker',  # Your database name
#         'USER': 'market_price_tracker_user',  # Your database username
#         'PASSWORD': '5hy8Q9NUDTgFZT1uBlMKxYsId6e0Lhbp',  # Your database password
#         'HOST': 'dpg-crk66hg8fa8c73fqgdcg-a',  # Your database host
#         'PORT': '5432',  # PostgreSQL's default port
#     }
# }




DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://market_price_tracker_user:5hy8Q9NUDTgFZT1uBlMKxYsId6e0Lhbp@dpg-crk66hg8fa8c73fqgdcg-a.oregon-postgres.render.com/market_price_tracker'
    )
}



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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
