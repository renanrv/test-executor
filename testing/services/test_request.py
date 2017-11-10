# -*- coding: utf-8 -*-
from testing.models.test_request import TestRequest


class TestRequestService():

    @classmethod
    def get_all_test_requests(cls):
        return TestRequest.objects.all()
