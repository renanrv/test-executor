# -*- coding: utf-8 -*-
from rest_framework import serializers


class TemplateSerializer(serializers.Serializer):
    name = serializers.CharField()

    class Meta:
        fields = ('name',)
        api_filter_name = 'default'
