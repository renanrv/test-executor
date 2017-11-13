# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MainTestCase(APITestCase):
    fixtures = ['environment.json']

    def test_get_environment_list(self):
        url = reverse('rest-api:environment-list')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for environment in response.data:
            self.assertIn('id', environment)
            self.assertIn('is_available', environment)

    def test_get_environment_detail(self):
        url = reverse('rest-api:environment-detail', args=(1,))
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        environment = response.data
        self.assertIn('id', environment)
        self.assertIn('is_available', environment)
