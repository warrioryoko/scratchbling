from django.conf.urls import patterns, include, url
from tastypie.api import Api
from scratchers.resources import ScratcherResource
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ScratcherResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
