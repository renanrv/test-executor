# -*- coding: utf-8 -*-
# Use this file as a basis for your local settings file.
# If you name it 'local.py', it will be used as the project's settings file automatically.
# If you use a different name, set the DJANGO_SETTINGS_MODULE environment variable
# to point to it (in Python dotted format).

# Pick one of the base settings files below, and remove the other lines:
from .development import *  # @UnusedWildImport

DEBUG = True
SERVE_STATIC_FILES_IN_DEBUG_FALSE = True

# Database settings.
DATABASES = {
    'default': {
        'NAME': 'testexecutordb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
        'ENGINE': 'django.db.backends.mysql',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

CACHES = {
    DEFAULT_CACHE: {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211'
    }
}

LOCAL_HOST_NAME = "localhost:8000"

ADMIN_HOST_NAME = LOCAL_HOST_NAME
HOST_NAME = LOCAL_HOST_NAME

STATIC_URL = 'http://%s/static/' % LOCAL_HOST_NAME
MEDIA_URL = 'http://%s/media/' % LOCAL_HOST_NAME

# Session settings.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, 'static-collected'))
