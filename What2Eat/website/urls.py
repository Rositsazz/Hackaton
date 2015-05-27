from django.conf.urls import url, patterns


urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),
    url(r'register/$', 'register', name='register'),
    url(r'signin/$', 'signin', name='signin'),
    url(r'logged/$', 'logged', name='logged'),
    url(r'dummy/$', 'dummy', name='dummy'),
    url(r'userlogout/$', 'userlogout', name='userlogout'),
)
