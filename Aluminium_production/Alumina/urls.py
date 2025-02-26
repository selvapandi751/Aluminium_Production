from django.contrib import admin
from django.urls import path,include
from Alumina import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('/userlog',views.userlog,name='userlog'),
    path('/register',views.register,name="register"),
    path('/adminlog',views.adminlog,name='adminlog'),
    path('/adminhome',views.adminhome,name="adminhome"),
    path('/pending_details',views.pending_details,name="pending_details"),
    path('/approved_details',views.approved_details,name='approved_details'),
    path('/approve/<int:id>',views.approve,name='approve'),
    path('/dissmiss/<int:id>',views.dissmiss,name='dissmiss'),
    path('/homepage',views.homepage,name="homepage"),
    path('/calculation',views.calculation,name="calculation")
]