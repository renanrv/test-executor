"""test-executor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve as staticfiles_serve
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from urllib.parse import urlparse
import re


API_TITLE = 'Test Executor API'
API_DESCRIPTION = 'A Web API for running and managing Python-based tests'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-api/', include('api.urls', namespace='rest-api')),
    url(r'^rest-api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG or settings.SERVE_STATIC_FILES_IN_DEBUG_FALSE:
    def extract_path(prefix):
        prefix = urlparse(prefix).path
        if prefix[0] == '/':
            prefix = prefix[1:]
        return prefix

    def django_serve_patterns(prefix, root):
        prefix = extract_path(prefix)
        regex = r'^%s(?P<path>.*)$' % prefix
        return [url(regex, serve, {'document_root': root})]

    def staticfiles_serve_patterns(prefix):
        prefix = extract_path(prefix)
        kwargs = {'insecure': True}
        return [url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), staticfiles_serve, kwargs=kwargs)]

    urlpatterns += django_serve_patterns(settings.MEDIA_URL, settings.MEDIA_ROOT)
    urlpatterns += staticfiles_serve_patterns(settings.STATIC_URL)
