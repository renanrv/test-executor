# -*- coding: utf-8 -*-
from rest_framework import serializers
from testing.models.environment import Environment


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ('id', 'is_available')
        api_filter_name = 'default'

    @classmethod
    def get_serializer_queryset(cls):
        return Environment.objects.all()
