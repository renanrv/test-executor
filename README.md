# test-executor
A web application that provides a central place to run Python-based tests.

Supported test runners:

* unittest
* py.test
* nose
* Django TestCase

# Dependencies:

* MySQL
* Memcached
* RabbitMQ
* Python 3.6
* Virtualenv (optional)


# Setup

* `$ git clone https://github.com/renanrv/test-executor.git
`
* `$ mkvirtualenv test-executor`
* `$ cd test-executor`
* `$ pip install -r requirements.txt`
* `$ Optional custom settings: main/settings.py`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
* `$ celery -A main worker -Q log`

# Tests:
    ./manage.py test test.test_test_request_api
    ./manage.py test test.test_environment_api

Sample tests for each test runner is available in /test