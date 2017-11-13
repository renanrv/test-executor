# -*- coding: utf-8 -*-
from api.views.testing.environment import EnvironmentViewSet
from api.views.testing.test_request import TestRequestViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
]

router = DefaultRouter(trailing_slash=False)
router.register(r'environment', EnvironmentViewSet, 'environment')
router.register(r'test-request', TestRequestViewSet, 'test-request')

urlpatterns += router.urls
