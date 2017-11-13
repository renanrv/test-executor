# -*- coding: utf-8 -*-
from api.serializers.testing.environment import EnvironmentSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from testing.services.environment import EnvironmentService


class EnvironmentViewSet(ModelViewSet):
    serializer_class = EnvironmentSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return EnvironmentService.get_all_environments()
