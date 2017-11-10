# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MainTestCase(APITestCase):
    fixtures = ['environment.json', 'requester.json', 'test_request.json']

    def test_get_test_request_list(self):
        url = reverse('rest-api:test-request-list')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for test_request in response.data:
            self.assertIn('id', test_request)
            self.assertIn('created_on', test_request)
            self.assertIn('template', test_request)
            self.assertIn('status', test_request)
            self.assertIn('environment', test_request)
            self.assertIn('requester', test_request)

    def test_get_test_request_detail(self):
        url = reverse('rest-api:test-request-detail', args=(1,))
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_request = response.data
        self.assertIn('id', test_request)
        self.assertIn('created_on', test_request)
        self.assertIn('template', test_request)
        self.assertIn('status', test_request)
        self.assertIn('environment', test_request)
        self.assertIn('requester', test_request)
