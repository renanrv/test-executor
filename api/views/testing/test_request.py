# -*- coding: utf-8 -*-
from api.serializers.testing.test_request import TestRequestSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from testing.services.test_request import TestRequestService


class TestRequestViewSet(ModelViewSet):
    default_serializer = TestRequestSerializer
    serializers = [TestRequestSerializer]
    serializer_class = TestRequestSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return TestRequestService.get_all_test_requests()
