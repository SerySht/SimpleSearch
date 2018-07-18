from django.conf.urls import include, url
from django.contrib import admin
import searching_engine

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('searching_engine.urls')),
]
