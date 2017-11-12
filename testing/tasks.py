# -*- coding: utf-8 -*-
from main.celery import celery_app
import sys
import traceback


def countdown(attempts):
    return 2 ** attempts


@celery_app.task(bind=True, max_retries=10)
def execute_test_request(self, test_request_id, template_for_execution):
    from testing.services.test_request import TestRequestService
    try:
        test_request = TestRequestService.get_test_request_by_id(test_request_id)
        TestRequestService.run_test_request(test_request, template_for_execution)
        return True
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        self.retry(countdown=countdown(self.request.retries), exc=e)
