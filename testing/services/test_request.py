# -*- coding: utf-8 -*-
from datetime import datetime
from os import listdir
from os.path import isfile, join
from testing.choices import TEST_REQUEST_STATUS_CHOICES, TEST_RUNNER_CHOICES
from testing.constants import TEST_TEMPLATES_PATH, TEST_REQUEST_LOG_FILENAME, \
    EXECUTION_TEST_TEMPLATES_PATH
from testing.models.test_request import TestRequest
from testing.services.environment import EnvironmentService
from testing.services.requester import RequesterService
from testing.value_objects import TemplateValueObject
import io
import subprocess
import sys


class TestRequestService():

    @classmethod
    def check_if_test_request_log_displays_success(cls, test_request):
        if (test_request.test_runner == cls._get_pytest_test_runner() and
                "FAILURES" not in test_request.log) or \
                (test_request.test_runner != cls._get_pytest_test_runner() and
                 "OK" in test_request.log):
            return True
        return False

    @classmethod
    def create_test_request(cls, serialized_test_request):
        custom_path = serialized_test_request.validated_data.get('custom_path')
        environment_id = serialized_test_request.validated_data.get('environment')
        requester_name = serialized_test_request.validated_data.get('requester')
        template = serialized_test_request.validated_data.get('template')

        # TODO: check if environment is available
        test_request = cls._save_test_request(environment_id,
                                              requester_name,
                                              template,
                                              custom_path)

        template_for_execution = cls._get_test_request_template_for_execution(test_request,
                                                                              template,
                                                                              custom_path)
        cls._run_test(test_request, template_for_execution)
        return test_request

    @classmethod
    def get_available_templates(cls):
        available_templates = []
        for template_file in listdir(TEST_TEMPLATES_PATH):
            if isfile(join(TEST_TEMPLATES_PATH, template_file)) and template_file.startswith("test"):
                available_templates.append(TemplateValueObject(name=template_file))
        return available_templates

    @classmethod
    def get_all_test_requests(cls):
        return TestRequest.objects.all()

    @classmethod
    def get_test_request_by_id(cls, test_request_id):
        return TestRequest.objects.filter(id=test_request_id).first()

    @classmethod
    def get_test_request_log(cls, test_request):
        filename = TEST_REQUEST_LOG_FILENAME % test_request.id
        log = ""
        try:
            with io.open(filename, 'rb', 1) as reader:
                log += reader.read().decode(sys.stdout.encoding)
        except FileNotFoundError:
            log = test_request.log
        test_request.log = log
        return test_request

    @classmethod
    def _get_django_testcase_test_runner(cls):
        return TEST_RUNNER_CHOICES[3][0]

    @classmethod
    def _get_failed_status(cls):
        return TEST_REQUEST_STATUS_CHOICES[2][0]

    @classmethod
    def _get_nose_test_runner(cls):
        return TEST_RUNNER_CHOICES[2][0]

    @classmethod
    def _get_pytest_test_runner(cls):
        return TEST_RUNNER_CHOICES[1][0]

    @classmethod
    def _get_requested_status(cls):
        return TEST_REQUEST_STATUS_CHOICES[0][0]

    @classmethod
    def _get_suceeded_status(cls):
        return TEST_REQUEST_STATUS_CHOICES[1][0]

    @classmethod
    def _get_test_request_template_for_execution(cls, test_request, template, custom_path):
        template = EXECUTION_TEST_TEMPLATES_PATH + template
        if custom_path is None or custom_path == "":
            template_for_execution = template
        else:
            template_for_execution = EXECUTION_TEST_TEMPLATES_PATH + custom_path

        if test_request.test_runner == cls._get_django_testcase_test_runner():
            template_for_execution = template_for_execution.replace("/", ".")
            if len(template_for_execution) > 3 and template_for_execution[-3:] == ".py":
                template_for_execution = template_for_execution[:-3]
        return template_for_execution

    @classmethod
    def _get_test_request_template_from_template_and_custom_path(cls, template, custom_path):
        if custom_path is None or custom_path == "":
            return template
        else:
            return "Custom test directory: %s" % custom_path

    @classmethod
    def _get_test_runner_command(cls, test_request, template):
        command = []
        if test_request.test_runner == cls._get_unittest_test_runner():
            command.append(sys.executable)
            command.append("-m")
            command.append("unittest")
            command.append("-v")
            command.append(template)
        elif test_request.test_runner == cls._get_pytest_test_runner():
            command.append(sys.executable)
            command.append("-m")
            command.append("pytest")
            command.append("-v")
            command.append(template)
        elif test_request.test_runner == cls._get_nose_test_runner():
            command.append(sys.executable)
            command.append("-m")
            command.append("nose")
            command.append("-v")
            command.append(template)
        elif test_request.test_runner == cls._get_django_testcase_test_runner():
            command.append(sys.executable)
            command.append("manage.py")
            command.append("test")
            command.append(template)
        return command

    @classmethod
    def _get_unittest_test_runner(cls):
        return TEST_RUNNER_CHOICES[0][0]

    @classmethod
    def _run_test(cls, test_request, template):
        filename = TEST_REQUEST_LOG_FILENAME % test_request.id
        command = cls._get_test_runner_command(test_request, template)
        log = ""
        with io.open(filename, 'wb') as writer, io.open(filename, 'rb', 1) as reader:
            process = subprocess.Popen(command, stdout=writer, stderr=writer)
            while process.poll() is None:
                log += reader.read().decode(sys.stdout.encoding)
            reader.read()
        test_request.log = log
        if cls.check_if_test_request_log_displays_success(test_request):
            test_request.status = cls._get_suceeded_status()
        else:
            test_request.status = cls._get_failed_status()
        test_request.save(update_fields=['status', 'log'])

    @classmethod
    def _save_test_request(cls, environment_id, requester_name, template, custom_path):
        test_request = TestRequest()
        test_request.environment = \
            EnvironmentService.get_environment_by_id(environment_id)
        test_request.requester = \
            RequesterService.get_or_create_requester_by_name(requester_name)
        test_request.created_on = datetime.now()
        test_request.template = \
            cls._get_test_request_template_from_template_and_custom_path(template,
                                                                         custom_path)
        test_request.status = cls._get_requested_status()
        test_request.save()
        return test_request
