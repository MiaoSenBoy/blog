#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redir),
    url(r'^index_(\d+)/$', views.index),
    url(r'^about/$', views.about),
    url(r'^post/$', views.post),
    url(r'^contact/$', views.contact),
    url(r'^write_blog/$', views.write_blog),
    url(r'^get_blog/$', views.get_blog),
    url(r'delete_blog/$', views.delete_blog),
    url(r'blog_detailed_(\d+)/$', views.blog_detailed),
    url(r'blog_validation(\d+)/$', views.blog_validation),
    url(r'delete_validation(\d+)/$', views.delete_validation),
    url(r'search/$', views.search),
]
