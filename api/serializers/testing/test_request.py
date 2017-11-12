# -*- coding: utf-8 -*-
from rest_framework import serializers
from testing.models.test_request import TestRequest


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class TestRequestQuerySerializer(serializers.Serializer):
    template = serializers.CharField()
    custom_path = serializers.CharField()
    envrionment = serializers.IntegerField()
    requester = serializers.CharField()


class TestRequestSerializer(serializers.ModelSerializer):
    test_runner = CodeSerializer(source='test_runner_value_object')
    status = CodeSerializer(source='status_value_object')
    requester = serializers.CharField(source='requester.name')

    class Meta:
        model = TestRequest
        fields = ('id', 'created_on', 'template', 'status', 'environment',
                  'requester', 'test_runner', 'log')
        api_filter_name = 'default'

    @classmethod
    def get_serializer_queryset(cls):
        return TestRequest.objects.all()
