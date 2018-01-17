from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from . import forms
from . import models

User = get_user_model()


class LoginView(bracesviews.AnonymousRequiredMixin,
                authviews.LoginView):
    template_name = "accounts/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        redirect = super(LoginView, self).form_valid(form)
        remember_me = form.cleaned_data.get('remember_me')
        if remember_me is True:
            ONE_MONTH = 30*24*60*60
            expiry = getattr(settings, "KEEP_LOGGED_DURATION", ONE_MONTH)
            self.request.session.set_expiry(expiry)
        return redirect


class LogoutView(authviews.LogoutView):
    url = reverse_lazy('home')

def radial_chart(request):
    
    obj = Profile.objects.get(name=str(request.user.username))
    json_data = {
		'aptus_cand': obj.aptus_cand,
		'latus_cand': obj.latus_cand,
		'tekne_cand': obj.tekne_cand,
		'personalis_cand': obj.personalis_cand,
		'aptus_avg': obj.aptus_avg,
		'latus_avg': obj.latus_avg,
		'tekne_avg': obj.tekne_avg,
		'personalis_avg': obj.personalis_avg,
		'aptus_highest': obj.aptus_highest,
		'latus_highest': obj.latus_highest,
		'tekne_highest': obj.tekne_highest,
		'personalis_highest': obj.personalis_highest
	}
    return JsonResponse(json_data)	

