# -*- coding: utf-8 -*-
from django.db import models
from testing.choices import TEST_REQUEST_STATUS_CHOICES
from testing.value_objects import StatusValueObject


class TestRequest(models.Model):
    requester = models.ForeignKey('testing.Requester', verbose_name=u"requester")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=u"creation date")
    environment = models.ForeignKey('testing.Environment', verbose_name=u"environment")
    template = models.CharField(max_length=255, verbose_name=u"template")
    status = models.IntegerField(choices=TEST_REQUEST_STATUS_CHOICES, verbose_name=u"status")

    class Meta:
        verbose_name = u"Test Request"
        verbose_name_plural = u"Test Requests"

    def __str__(self):
        return "#%d - %s - %s" % (self.id, self.template, self.created_on)

    @property
    def status_value_object(self):
        return StatusValueObject(code=self.status,
                                 name=TEST_REQUEST_STATUS_CHOICES[self.status][1])