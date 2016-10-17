from django.conf.urls import url

from . import views

app_name = 'Beehive'
urlpatterns = [
    url(r'^$', views.index, name='content-index'),
    url(r'^skills/$', views.skill, name='skills'),
    url(r'^skills/(?P<skill_id>[0-9]+)/$', views.view_skill, name='skill'),
    url(r'^$', views.dashboard, name='Beehive-dashboard'),
    url(r'^home/$', views.home, name='Beehive-home'),
    url(r'^create-account/$', views.create_user, name="create-account" ),
    url(r'^(?P<article_id>[0-9]+)/$', views.view_article, name='content-view_article'),
    url(r'^(?P<skill_id>[0-9]+)/$', views.view_skill, name='content-view_skill')
]
