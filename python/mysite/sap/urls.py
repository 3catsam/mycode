from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'sap.views.first_page'),
)
