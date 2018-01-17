from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import forms
from . import models
from profiles.models import Profile
from profiles.models import MainProfile
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse



class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)


def radial_chart(request):
    
    obj = MainProfile.objects.get(email=str(request.user.email))
    json_data = {
		'aptus_cand': obj.aptus_cand,
		'latus_cand': obj.latus_cand,
		'tekhne_cand': obj.tekhne_cand,
		'aptus_avg': obj.aptus_avg,
		'latus_avg': obj.latus_avg,
		'tekhne_avg': obj.tekhne_avg,
		'aptus_highest': obj.aptus_highest,
		'latus_highest': obj.latus_highest,
		'tekhne_highest': obj.tekhne_highest,
	}
    return JsonResponse(json_data)	


def user_data(request):
    
    obj = MainProfile.objects.get(email=str(request.user.email))
    json_data = {
        'name': obj.name,
        'registration_no': obj.registration_no,
        'college': obj.college,
        'email': obj.email,
        'test_date': obj.test_date,
        'valid_till': obj.valid_till,
        'overall_percentile': obj.overall_percentile,
        'aptus_percentile': obj.aptus_percentile,
        'latus_percentile': obj.latus_percentile,
        'tekhne_percentile': obj.tekhne_percentile,
        'personalis_code': obj.personalis_code        
    }
    return JsonResponse(json_data)  

