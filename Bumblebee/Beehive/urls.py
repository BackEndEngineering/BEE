from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='content-index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.view_article, name='content-view_article')
]
]
