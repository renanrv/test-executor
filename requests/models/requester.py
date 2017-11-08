# -*- coding: utf-8 -*-
from django.db import models


class Requester(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"name")

    class Meta:
        verbose_name = u"Requester"
        verbose_name_plural = u"Requesters"

    def __str__(self):
        return "#%d - %s" % (self.id, self.name)
