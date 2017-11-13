# -*- coding: utf-8 -*-
from testing.models.environment import Environment


class EnvironmentService():

    @classmethod
    def check_if_environment_is_available(cls, environment):
        """Return True if environment is available for test execution."""
        if environment.is_available:
            return True
        return False

    @classmethod
    def get_environment_by_id(cls, environment_id):
        """Return environment by ID."""
        return Environment.objects.filter(id=environment_id).first()

    @classmethod
    def get_available_environments(cls):
        """Return available environments."""
        return Environment.objects.filter(is_available=True)

    @classmethod
    def get_all_environments(cls):
        """Return all environments from database."""
        return Environment.objects.all()

    @classmethod
    def set_environment_available(cls, environment):
        """Set environment as available."""
        environment.is_available = True
        environment.save(update_fields=["is_available"])

    @classmethod
    def set_environment_not_available(cls, environment):
        """Set environment as not available."""
        environment.is_available = False
        environment.save(update_fields=["is_available"])
