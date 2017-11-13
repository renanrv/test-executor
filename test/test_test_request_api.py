# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch


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
            self.assertIn('test_runner', test_request)
            self.assertIn('log', test_request)

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
        self.assertIn('test_runner', test_request)
        self.assertIn('log', test_request)

    def test_get_test_request_log(self):
        url = reverse('rest-api:test-request-log', args=(1,))
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
        self.assertIn('test_runner', test_request)
        self.assertIn('log', test_request)

    def test_get_test_templates_list(self):
        url = reverse('rest-api:test-request-template')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for test_request in response.data:
            self.assertIn('name', test_request)

    def test_get_test_runners_list(self):
        url = reverse('rest-api:test-request-test-runner')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for test_request in response.data:
            self.assertIn('code', test_request)
            self.assertIn('name', test_request)

    @patch('testing.services.test_request.TestRequestService._execute_test_command',
           lambda x, y: None)
    def test_create_test_request(self):
        url = reverse('rest-api:test-request-list')
        data = {"template": "test_test_request_api.py",
                "environment": 1,
                "requester": "Test",
                "test_runner": 3}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        test_request = response.data
        self.assertIn('id', test_request)
        self.assertIn('created_on', test_request)
        self.assertIn('template', test_request)
        self.assertIn('status', test_request)
        self.assertIn('environment', test_request)
        self.assertIn('requester', test_request)
        self.assertIn('test_runner', test_request)
        self.assertIn('log', test_request)
