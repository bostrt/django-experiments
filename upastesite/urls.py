from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from upastesite import views
from upastesite.models import Paste

urlpatterns = patterns('',
  #url(r'^$', views.index, name='index'),
  url(r'^$', 
      ListView.as_view(
            queryset=Paste.objects.order_by('-added')[:5],
            context_object_name='latest_paste_list',
            template_name='upastesite/index.html'),
      name='index'),
  url(r'^paste/$', views.new_paste, name='new_paste'),
  #url(r'^paste/(?P<paste_id>\d+)/$', views.paste, name='paste'),
  url(r'^paste/(?P<pk>\d+)/$',
      DetailView.as_view(
            model=Paste,
            template_name='upastesite/paste.html'),
      name='paste'),
)
