# -*- coding: utf-8 -*-


class StatusValueObject(object):
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name


class TemplateValueObject(object):
    def __init__(self, name=None):
        self.name = name


class TestRunnerValueObject(object):
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name
