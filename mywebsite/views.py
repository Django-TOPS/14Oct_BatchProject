from django.shortcuts import render, HttpResponse, redirect, Http404
from .forms import signupForm, uploadpostForm
from .models import signup
from django.core.mail import send_mail
from site1 import settings
from django.contrib.auth import logout
import random

# Create your views here.


def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            myfrm=signupForm(request.POST)
            if myfrm.is_valid():
                myfrm.save()
                print("Signup Successfully!")

                """
                # Send MAIL
                otp=random.randint(11111,99999)
                subject='Django Testing Mail'
                msg=f'Hello Student, Your account has been created successfully! Your one time password is {otp} '
                from_id=settings.EMAIL_HOST_USER
                to_id=['kishanchavda909@gmail.com','prakashbhajgotar53@gmail.com','nehal.pan17@gmail.com','mirudobariya18@gmail.com','meetdetroja123@gmail.com']
                
                send_mail(subject,msg,from_id,to_id)
                """    

                return redirect('profile')
            else:
                print(myfrm.errors)

        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']
            uid=signup.objects.get(username=unm)    
            user=signup.objects.filter(username=unm,password=pas)

            if user:
                request.session['userid']=unm
                request.session['uid']=uid.id
                print('Login Successfully!')
                return redirect('profile')
            else:
                print("Error...Login Faild.")
    else:
        myfrm=signupForm()

    return render(request,'index.html',{'myfrm':myfrm})

def profile(request):
    user=request.session.get('userid')
    if request.method=='POST':
        if request.POST.get('submitpost')=='submitpost':
            uploadfrm=uploadpostForm(request.POST,request.FILES)

            if uploadfrm.is_valid():
                uploadfrm.save()
                print("Your post has been uploaded!")
            else:
                print(uploadfrm.errors)

        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']
            #uid=signup.objects.get(username=unm)   

            user=signup.objects.filter(username=unm,password=pas)

            if user:
                request.session['userid']=unm
                #request.session['uid']=uid.id
                print('Login Successfully!')
                return redirect('profile')
            else:
                print("Error...Login Faild.")
    else:
        uploadfrm=uploadpostForm()
    return render(request,'profile.html',{'user':user,'uploadfrm':uploadfrm})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def updatedata(request,id):
    if request.method=='POST':
        #myfrm=signupForm()
        id=signup.objects.get(id=id)
        myfrm=signupForm(request.POST, instance=id) 
        if myfrm.is_valid():
            myfrm.save()
            print("Your profile has been updated!")
            return redirect('profile')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupForm()
    return render(request,'updateprofile.html',{'myfrm':myfrm,'userdata':signup.objects.get(id=id)})

def studentdata(request):
    user=request.session.get('userid')
    if request.method=='POST':
        #id=signup.objects.get(id)
        myfrm=signupForm(request.POST, instance=id) 
        if myfrm.is_valid():
            myfrm.save()
            print("Your profile has been updated!")
            return redirect('profile')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupForm()
    return render(request,'studentdata.html',{'myfrm':myfrm,'userdata':signup.objects.all,'user':user})
    
def deletedata(request, id):
    userid=signup.objects.get(id=id)
    userid.delete()
    return redirect('profile')
    return render(request,'studentdata.html',{'userdata':signup.objects.all})

def upadteprofile(request):
    user_id=request.session.get('uid')
    usid=request.session.get('userid')
    if request.method=='POST':
        #myfrm=signupForm()
        id=signup.objects.get(id=user_id)
        myfrm=signupForm(request.POST, instance=id) 
        if myfrm.is_valid():
            myfrm.save()
            print("Your profile has been updated!")
            return redirect('profile')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupForm()
    return render(request,'updateprofile.html',{'myfrm':myfrm, 'userdata':signup.objects.get(id=user_id),'usid':usid})