# -*- coding: utf-8 -*-
from testing.models.requester import Requester


class RequesterService():

    @classmethod
    def get_requester_by_id(cls, requester_id):
        return Requester.objects.filter(id=requester_id).first()

    @classmethod
    def get_or_create_requester_by_name(cls, name):
        requester, _ = Requester.objects.get_or_create(name=name)
        return requester

    @classmethod
    def get_all_requesters(cls):
        return Requester.objects.all()
