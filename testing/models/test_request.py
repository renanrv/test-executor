# -*- coding: utf-8 -*-
from django.db import models
from testing.choices import TEST_REQUEST_STATUS_CHOICES, TEST_RUNNER_CHOICES
from testing.value_objects import StatusValueObject, TestRunnerValueObject


class TestRequest(models.Model):
    requester = models.ForeignKey('testing.Requester', verbose_name=u"requester")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=u"creation date")
    environment = models.ForeignKey('testing.Environment', verbose_name=u"environment")
    test_runner = models.IntegerField(choices=TEST_RUNNER_CHOICES, verbose_name=u"test runner")
    template = models.CharField(max_length=255, verbose_name=u"template")
    status = models.IntegerField(choices=TEST_REQUEST_STATUS_CHOICES, verbose_name=u"status")
    log = models.TextField(null=True, blank=True, verbose_name=u"log")

    class Meta:
        verbose_name = u"Test Request"
        verbose_name_plural = u"Test Requests"

    def __str__(self):
        return "#%d - %s - %s" % (self.id, self.template, self.created_on)

    @property
    def status_value_object(self):
        """Return a value object representing the test request status field."""
        return StatusValueObject(code=self.status,
                                 name=TEST_REQUEST_STATUS_CHOICES[self.status][1])

    @property
    def test_runner_value_object(self):
        """Return a value object representing the test request test runner field."""
        return TestRunnerValueObject(code=self.test_runner,
                                     name=TEST_RUNNER_CHOICES[self.test_runner][1])
