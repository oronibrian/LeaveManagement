"""EmployeeLeavemanagement URL Configuration
"""

from django.contrib import admin
from django.urls import path,include
from Leave import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    # path('apply/', views.createLeave, name='apply'),

]
