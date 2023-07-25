from .base import *
import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wc(h!52&er7dpz_nkq3kk*bjf&ti^$jz)%m(+xtp0hlkwo_lp-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}
