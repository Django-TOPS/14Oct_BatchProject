from django.contrib import admin
from django.urls import path,include
from mywebsite import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('',views.index),
    path('profile/',views.profile,name='profile'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('user_logout',views.user_logout),
    path('updatedata/<int:id>',views.updatedata),
    path('studentdata/',views.studentdata,name='studentdata'),
    path('deletedata/<int:id>',views.deletedata),
    path('updateprofile/',views.upadteprofile),

]