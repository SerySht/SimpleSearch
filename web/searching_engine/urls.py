from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),

    url(r'^indexURL', views.index_url, name='indexURL'),
    url(r'^knownURL', views.knownURL, name='knownURL'),
    url(r'^indexWords', views.indexWords, name='indexWords'),
]
