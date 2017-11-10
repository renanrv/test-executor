# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from testing.models.test_request import TestRequest


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class TestRequestSerializer(serializers.ModelSerializer):
    status = CodeSerializer(source='status_value_object')
    requester = serializers.CharField(source='requester.name')

    class Meta:
        model = TestRequest
        fields = ('id', 'created_on', 'template', 'status', 'environment',
                  'requester')
        api_filter_name = 'default'

    @classmethod
    def get_serializer_queryset(cls):
        return TestRequest.objects.all()

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(self)

    def update(self, instance, validated_data):
        raise MethodNotAllowed(self)
