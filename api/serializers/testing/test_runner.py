# -*- coding: utf-8 -*-
from rest_framework import serializers


class TestRunnerSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    name = serializers.CharField()
