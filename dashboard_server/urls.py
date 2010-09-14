from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib import databrowse
from django.views.generic.simple import direct_to_template

from dashboard_app.views import dashboard_xml_rpc_handler
from dashboard_app.models import (
    Bundle,
    BundleStream,
    HardwareDevice,
    NamedAttribute,
    SoftwarePackage,
    Test,
    TestCase,
    TestRun
)

# Register our models with data browser
databrowse.site.register(Bundle)
databrowse.site.register(BundleStream)
databrowse.site.register(HardwareDevice)
databrowse.site.register(NamedAttribute)
databrowse.site.register(SoftwarePackage)
databrowse.site.register(Test)
databrowse.site.register(TestCase)
databrowse.site.register(TestRun)

# Enable admin stuff
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template,
        name='home',
        kwargs={'template': 'index.html'}),
    url(r'^about-alpha/', direct_to_template,
        name='about-alpha',
        kwargs={'template': 'about_alpha.html'}),
    url(r'^xml-rpc/', dashboard_xml_rpc_handler,
        name='xml-rpc-handler'),
    url(r'^databrowse/(.*)', databrowse.site.root),
    (r'^admin/', include(admin.site.urls)),
    )

if not settings.CONFIGURED:
    # This is only used when we cannot count on static media files being
    # served by some real web server. WARNING: this is not secure and
    # should _never_ be used in production environments.
    # See:
    # http://docs.djangoproject.com/en/1.2/howto/static-files/#the-big-fat-disclaimer)
    urlpatterns += patterns('',
            (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True}))

