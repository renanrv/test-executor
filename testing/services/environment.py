# -*- coding: utf-8 -*-
from testing.models.environment import Environment


class EnvironmentService():

    @classmethod
    def check_if_environment_is_available(cls, environment):
        if environment.is_available:
            return True
        return False

    @classmethod
    def get_environment_by_id(cls, environment_id):
        return Environment.objects.filter(id=environment_id).first()

    @classmethod
    def get_available_environments(cls):
        return Environment.objects.filter(is_available=True)

    @classmethod
    def get_all_environments(cls):
        return Environment.objects.all()

    @classmethod
    def set_environment_available(cls, environment):
        environment.is_available = True
        environment.save(update_fields=["is_available"])

    @classmethod
    def set_environment_not_available(cls, environment):
        environment.is_available = False
        environment.save(update_fields=["is_available"])
