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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from httpbucket import views as httpbucket_views
from httpbucket import view_sets as httpbucket_view_sets
from registration import view_sets as registration_view_sets

router = routers.DefaultRouter()
router.register(r'users', registration_view_sets.UserViewSet)
router.register(r'drf_entries', httpbucket_view_sets.RequestLogEntryViewSet)

urlpatterns = [
    url(r'^$', httpbucket_views.hello_world),
    url(r'^my_entries/$', httpbucket_views.RequestLogEntryListView.as_view(), name='my_entries'),
    url(r'^my_entries_json/$', login_required(httpbucket_views.MyEntriesJSONView.as_view()), name='my_entries_json'),
    url(r'^my_entries_oauth2/$', login_required(httpbucket_views.MyEntriesOAuth2View.as_view()), name='my_entries_oauth2'),
    url(r'^get/$', csrf_exempt(httpbucket_views.EchoView.as_view()), name='echo_get'),
    url(r'^get/(?P<pk>\d+)/$', httpbucket_views.RequestLogEntryDetailView.as_view(), name='replay_get'),
    url(r'^create/$', httpbucket_views.RequestLogEntryCreateView.as_view(), name='create_replay'),
    url(r'^admin/', admin.site.urls),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
]
