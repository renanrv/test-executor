# -*- coding: utf-8 -*-
from django.conf import settings
from django.test.runner import DiscoverRunner
from main.celery import celery_app


def _set_eager():
    settings.CELERY_ALWAYS_EAGER = True
    celery_app.conf.CELERY_ALWAYS_EAGER = True
    settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
    celery_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True


class CeleryTestSuiteRunner(DiscoverRunner):
    """Django test runner allowing testing of celery delayed tasks.
    All tasks are run locally, not in a worker.
    """
    def setup_test_environment(self, **kwargs):
        _set_eager()
        super(CeleryTestSuiteRunner, self).setup_test_environment(**kwargs)
