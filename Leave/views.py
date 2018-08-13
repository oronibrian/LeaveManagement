from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView
from .models import LeaveType,Leave
from .forms import LeaveForm
from django.core.mail import EmailMessage


@login_required(login_url='/accounts/login/')
def index(request):
	if request.method == 'POST':
	    form = LeaveForm(request.POST)
	    if form.is_valid():
	    	leave = form.save(commit = False)
	    	leave.user = request.user

	    	leave.save()
	    	sendMail(request)
	    	return HttpResponseRedirect('/')

	else:
	    form = LeaveForm()
	return render(request, 'index.html', {'form': form})



def sendMail(request):
	username = request.user
	email = EmailMessage('Leave Application', 'New Leave Application From ' +str(username), to=['brianoroni6@gmail.com'])
	email.send()
	return HttpResponseRedirect('/')
