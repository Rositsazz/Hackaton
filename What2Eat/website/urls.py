from django.conf.urls import url, patterns
# from django.conf.url import patterns


urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    # url(r'info/$', 'info'),
    # url(r'register/$', 'register'),
    # url(r'logout/$', 'logout'),
)
