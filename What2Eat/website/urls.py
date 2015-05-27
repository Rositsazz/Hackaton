
from django.conf.urls import url

# from django.conf.url import patterns

from . import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    # url(r"info/$".views.info, name="info"),
    # url(r"^register/$", views.register, name="register"),
    # url(r"^logout/$", views.chat_logout, name="logout"),
]
