from django.db import models
from django.contrib.auth.models import User
from datetime import date,datetime
# Create your models here.

LEAVE_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
)

class LeaveType(models.Model):
	name=models.CharField(max_length=500)
	desc=models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

def differ_days(date1, date2):

    a = date1
    b = date2
    return (a-b).days


class Leave(models.Model):
	date_format = "%m/%d/%Y"

	user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
	leave_type = models.ForeignKey(LeaveType,on_delete=models.CASCADE)
	start_date = models.DateField(null=False)
	end_date = models.DateField(null=True)

	days=models.IntegerField(default=differ_days((date(2016,10,12)), date(2015,12,10)))

	status= models.CharField(max_length=120, default='pending',choices=LEAVE_STATUS_CHOICES)

	def __str__(self):
	    return str(self.leave_type)



