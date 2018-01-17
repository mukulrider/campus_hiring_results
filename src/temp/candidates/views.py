from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from .models import Muapt_Scores

# Create your views here.

def first_page(request):
    
    context = {
        'object_list': Muapt_Scores.objects.filter(name=str(request.user.username))
    }
    print(context['object_list'])
	   
    return render(request,'candidates/home.html',context)
        
def radial_chart(request):
    
    obj = Muapt_Scores.objects.get(name=str(request.user.username))
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

def authentication(request):
    return render(request,'candidates/authentication.html')

def contact(request):
    return render(request,'candidates/contact.html', {'content':['Username/Password entered is incorrect!','If you believe this is in error, contact us at','mukul.gupta1@mu-sigma.com, mukulrider@gmail.com']})

	
def login_view(request):
	a = authenticate(username=str(request.POST['username']), password=str(request.POST['password']))
	print (a)
	user = authenticate(username=str(request.POST['username']), password=str(request.POST['password']))

	if user is not None:
		# the password verified for the user
		if user.is_active:
			print("User is valid, active and authenticated with %s" % request.user.username)
			login(request, user)
			return HttpResponseRedirect('/dashboard/')
		else:
			print("The password is valid, but the account has been disabled!")
	else:
		# the authentication system was unable to verify the username and password
		print("The username and password were incorrect.")	
		return HttpResponseRedirect('/contact/')
	
	