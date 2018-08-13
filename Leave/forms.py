from django import forms

from django.contrib.auth.models import User
from .models import Leave
from django.contrib.admin.widgets import AdminDateWidget


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class LeaveForm(forms.ModelForm):

	# start_date = forms.DateField(widget=forms.DateInput(format = '%m/%d/%Y'))
	# end_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'))


	class Meta:
	    model = Leave
	    fields = ("leave_type", "start_date", "end_date")
	    widgets = {
		    'end_date': forms.DateTimeInput(attrs={'class': 'datepicker'}),
		    'start_date': forms.DateTimeInput(attrs={'class': 'datepicker'})

		}


