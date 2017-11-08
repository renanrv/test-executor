# -*- coding: utf-8 -*-
from django.db import models


class Environment(models.Model):
    is_available = models.BooleanField(default=True, verbose_name=u"available?")

    class Meta:
        verbose_name = u"Environment"
        verbose_name_plural = u"Environments"

    def __str__(self):
        return "#%d" % self.id
