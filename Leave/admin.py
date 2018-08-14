from django.contrib import admin

from .models import LeaveType,Leave
from django.core.mail import EmailMessage



class LeaveAdmin(admin.ModelAdmin):
	list_display = ('start_date', 'leave_type','user','end_date','status')
	# specifies the order as well as which fields to act on
	# readonly_fields = ('start_date', 'end_date')

	actions = ['Approve', 'Reject']



	def Approve(self, request, queryset):
	    for Leave in queryset:
	        Leave.status = 'approved'
	        email=EmailMessage('Leave Approval','''our Leave Application has been approved.
		 You are required to report back on the end date''',to=['brianoroni6@gmail.com'])
	        email.send()
	        Leave.save()

	def Reject(self, request, queryset):
	    for Leave in queryset:
	        Leave.status = 'rejected'
	        Leave.save()


admin.site.register(LeaveType)
admin.site.register(Leave,LeaveAdmin)

