"""config URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from httpbucket import views as httpbucket_views

urlpatterns = [
    url(r'^$', httpbucket_views.hello_world),
    url(r'^get/$', csrf_exempt(httpbucket_views.EchoView.as_view())),
    url(r'^get/(?P<pk>\d+)/$', httpbucket_views.RequestLogEntryDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
]
