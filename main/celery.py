# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

from django.conf import settings

celery_app = Celery('main', backend='cache+memcached://%s/' % settings.DEFAULT_CACHE_LOCATION, broker='amqp://%s@%s//' % (settings.RABBITMQ_USER + ':' + settings.RABBITMQ_PASSWORD
                                                                                                                          if settings.RABBITMQ_PASSWORD is not None else settings.RABBITMQ_USER,
                                                                                                                          settings.RABBITMQ_HOST), include=['testing.tasks'])

celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
