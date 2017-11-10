# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
from testing.constants import TEST_TEMPLATES_PATH
from testing.models.test_request import TestRequest
from testing.value_objects import TemplateValueObject


class TestRequestService():

    @classmethod
    def get_available_templates(cls):
        available_templates = []
        for template_file in listdir(TEST_TEMPLATES_PATH):
            if isfile(join(TEST_TEMPLATES_PATH, template_file)):
                available_templates.append(TemplateValueObject(name=template_file))
        return available_templates

    @classmethod
    def get_all_test_requests(cls):
        return TestRequest.objects.all()
