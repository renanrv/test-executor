# -*- coding: utf-8 -*-
# Base settings for local developer instances.

from .base import *  # @UnusedWildImport
from django.core.servers import basehttp


DEBUG_CONSOLE_LOGGER = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': False,
}

basehttp.WSGIRequestHandler.log_message = lambda *args, **kwargs: None
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
