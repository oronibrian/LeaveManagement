from django.contrib import admin

from .models import LeaveType,Leave



class LeaveAdmin(admin.ModelAdmin):
	list_display = ('start_date', 'leave_type','user','end_date','status')
	# specifies the order as well as which fields to act on
	# readonly_fields = ('start_date', 'end_date')

	actions = ['Approve', 'Reject']

	def Approve(self, request, queryset):
	    for Leave in queryset:
	        Leave.status = 'approved'
	        Leave.save()

	def Reject(self, request, queryset):
	    for Leave in queryset:
	        Leave.status = 'rejected'
	        Leave.save()

admin.site.register(LeaveType)
admin.site.register(Leave,LeaveAdmin)