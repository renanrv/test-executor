# -*- coding: utf-8 -*-
from django.contrib import admin
from testing.models.environment import Environment
from testing.models.requester import Requester
from testing.models.test_request import TestRequest
from testing.tasks import execute_test_request
from testing.services.environment import EnvironmentService


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Requester)
class RequesterAdmin(admin.ModelAdmin):
    pass


@admin.register(TestRequest)
class TestRequestAdmin(admin.ModelAdmin):
    readonly_fields = ('status', 'log')

    def save_model(self, request, obj, form, change):
        from testing.services.test_request import TestRequestService
        template_for_execution = TestRequestService._get_test_request_template_for_execution(obj,
                                                                                             template=obj.template,
                                                                                             custom_path="")
        obj.status = TestRequestService.get_requested_status()
        obj.save()
        EnvironmentService.set_environment_not_available(obj.environment)
        execute_test_request.delay(obj.id, template_for_execution)
