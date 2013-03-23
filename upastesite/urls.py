from django.conf.urls import patterns, url

from upastesite import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^group/(?P<group_id>\d+)/$', views.group, name='group'),
                       url(r'^paste/$', views.new_paste, name='new_paste'),
                       url(r'^paste/(?P<paste_id>\d+)/$', views.paste, name='paste'),
)
