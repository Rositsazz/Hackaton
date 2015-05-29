from django.conf.urls import url, patterns


urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),
    url(r'register/$', 'register', name='register'),
    url(r'signin/$', 'signin', name='signin'),
    url(r'logged/$', 'logged', name='logged'),
    url(r'dummy/$', 'dummy', name='dummy'),
    url(r'userlogout/$', 'userlogout', name='userlogout'),
    url(r'findrecipe/$', 'findrecipe', name='findrecipe'),
    url(r'^get_suggested/$', 'get_suggested'),
    url(r'^get_suggested_recipes/$', 'get_suggested_recipes'),
    url(r'^find_suggested_recipes/(?P<recipe_id>[0-9]+)/$', 'find_suggested_recipes'),
    url(r'^openrecipe/(?P<recipe_id>[0-9]+)/$', 'openrecipe'),
    url(r'^profile/$', 'profile', name="profile"),
)
