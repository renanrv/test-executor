# -*- coding: utf-8 -*-
from api.serializers.testing.template import TemplateSerializer
from api.serializers.testing.test_request import TestRequestSerializer, \
    TestRequestQuerySerializer
from api.serializers.testing.test_runner import TestRunnerSerializer
from rest_framework.decorators import list_route, detail_route
from rest_framework.exceptions import NotFound
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from testing.services.test_request import TestRequestService


class TestRequestViewSet(ModelViewSet):
    serializer_class = TestRequestSerializer
    pagination_class = LimitOffsetPagination

    def create(self, request):
        query_serializer = TestRequestQuerySerializer(data=request.data)
        query_serializer.is_valid(raise_exception=True)

        test_request = TestRequestService.create_test_request(query_serializer)

        return Response(TestRequestSerializer(test_request).data,
                        status=status.HTTP_201_CREATED)

    @list_route(url_path='template')
    def get_test_templates(self, request):
        return Response(TemplateSerializer(TestRequestService.get_available_templates(),
                                           many=True).data)

    @list_route(url_path='test-runner')
    def get_test_runners(self, request):
        return Response(TestRunnerSerializer(TestRequestService.get_supported_test_runners(),
                                             many=True).data)

    @detail_route(url_path='log')
    def get_test_log(self, request, pk):
        test_request = TestRequestService.get_test_request_by_id(pk)
        if test_request is not None:
            return Response(TestRequestSerializer(TestRequestService.get_test_request_log(test_request)).data)
        return NotFound

    def get_queryset(self):
        return TestRequestService.get_all_test_requests()
