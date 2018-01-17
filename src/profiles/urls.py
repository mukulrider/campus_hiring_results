from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),

        name='show'),
    url(r'^d3data/$', views.radial_chart, name='radial_chart'),
	url(r'^userdata/$', views.user_data, name='userdata'),
]
