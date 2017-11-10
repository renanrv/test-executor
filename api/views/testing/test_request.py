# -*- coding: utf-8 -*-
from api.serializers.testing.template import TemplateSerializer
from api.serializers.testing.test_request import TestRequestSerializer
from rest_framework.decorators import list_route
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from testing.services.test_request import TestRequestService


class TestRequestViewSet(ModelViewSet):
    serializer_class = TestRequestSerializer
    pagination_class = LimitOffsetPagination

    @list_route(url_path='template')
    def get_test_templates(self, request):
        return Response(TemplateSerializer(TestRequestService.get_available_templates(),
                                           many=True).data)

    def get_queryset(self):
        return TestRequestService.get_all_test_requests()
