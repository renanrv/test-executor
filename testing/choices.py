# -*- coding: utf-8 -*-
TEST_REQUEST_STATUS_CHOICES = (
    (0, 'Requested'),
    (1, 'Succeeded'),
    (2, 'Failed'),
)

TEST_RUNNER_CHOICES = (
    (0, 'unittest'),
    (1, 'py.test'),
    (2, 'nose'),
    (3, 'Django TestCase'),
)
