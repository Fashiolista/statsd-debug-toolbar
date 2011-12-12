from django.conf.urls.defaults import patterns, include, url
from .views import demo_one

urlpatterns = patterns('',
    url(r'^one/$', demo_one)
)
