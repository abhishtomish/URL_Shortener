from django.urls import path
from django.conf.urls import url
from shortener.api.views import get_short_url_api, create_short_url_api

urlpatterns = [
    # url(r'^get/$',get_short_url_api),
    path('/api/', get_short_url_api, name='detail'),
    path('/create', create_short_url_api, name='create')
]