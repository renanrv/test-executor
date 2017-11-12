# -*- coding: utf-8 -*-
from testing.models.environment import Environment


class EnvironmentService():

    @classmethod
    def get_environment_by_id(cls, environment_id):
        return Environment.objects.filter(id=environment_id).first()

    @classmethod
    def get_available_environments(cls):
        return Environment.objects.filter(is_available=True)

    @classmethod
    def get_all_environments(cls):
        return Environment.objects.all()
