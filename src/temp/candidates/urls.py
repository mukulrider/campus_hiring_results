from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from . import views
from candidates.models import Muapt_Scores

urlpatterns = [
    url(r'^dashboard/$', views.first_page, name='first_page'),
	url(r'^d3data/$', views.radial_chart, name='radial_chart'),
    url(r'^$', views.authentication, name='authentication'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^candidate/', ListView.as_view(queryset=Muapt_Scores.objects.all().order_by("name")[:25],
                                          template_name="candidates/candidate_scores.html")),
    url(r'^candidate/1$', DetailView.as_view(model=Muapt_Scores,
                                                        template_name = "candiates/candidate_details.html")),
	url(r'^login/$', views.login_view, name='login'),
    ]

