from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm,FeedbackForm
from django.http import HttpResponse
from .models import RegData,FeedbackData

# Create your views here.
def regform_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('firstname')
            lname = request.POST.get('lastname')
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            data=RegData(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=pwd,
                mobile=mobile,
                email=email,
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'myapp/reg.html',{'rform':rform})
        else:
            return HttpResponse('user invalid data')
    else:
        rform=RegistrationForm()
        return render(request,'myapp/reg.html',{'rform':rform})

def login_view(request):
    if request.method=='POST':
       lform=LoginForm(request.POST)
       if lform.is_valid():
           uname=request.POST.get('username')
           pwd=request.POST.get('password')
           user=RegData.objects.filter(username=uname)
           password=RegData.objects.filter(password=pwd)
           if user and password:
                return redirect('/home')
           else:
                return HttpResponse('Fail')
       else:
           return HttpResponse('user invalid data')
    else:
        lform=LoginForm()
        return render(request,'myapp/login.html',{'lform':lform})
def home_view(request):
    return  render(request,'myapp/home.html')
def services_view(request):
    return  render(request,'myapp/services.html')
def contact_view(request):
    return  render(request,'myapp/contact.html')
import datetime as dt
date1=dt.datetime.now()
def feedback_view(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name =request.POST.get('name')
            rating = request.POST.get('rating')
            #date=request.POST.get('date')
            feedback= request.POST.get('feedback')

            data=FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback,
            )
            data.save()
            fform=FeedbackForm()
            data=FeedbackData.objects.all()
            return render(request,'myapp/feedback.html',{'fform':fform,'data':data})
        else:
            return HttpResponse('User Missed Some values')
    else:
      data=FeedbackData.objects.all()
      fform=FeedbackForm()
      return render(request,'myapp/feedback.html',{'fform':fform,'data':data})

def gallery_view(request):
    return  render(request,'myapp/gallery.html')

from .forms import ContactForm
from .models import ContactData

def contact_view(request):
    if request.method=='POST':
       cform=ContactForm(request.POST)
       if cform.is_valid():
           name=request.POST.get('name')
           mobile=request.POST.get('mobile')
           email=request.POST.get('email')

           courses=cform.cleaned_data.get('courses')
           trainers = cform.cleaned_data.get('trainers')
           branches=cform.cleaned_data.get('branches')
           date=cform.cleaned_data.get('date')
           gender=cform.cleaned_data.get('gender')
           data=ContactData(
               name=name,
               mobile=mobile,
               email=email,
               courses=courses,
               branches=branches,
               date=date,
               trainers=trainers,
               gender=gender,
           )
           data.save()
           cform=ContactForm()
           return render(request,'myapp/contact.html',{'cform':cform})
       else:
           return HttpResponse('invalid data')
    else:
     cform=ContactForm()
     return render(request,'myapp/contact.html',{'cform':cform})

from .models import CourseData
def course_view(request):
    courses=CourseData.objects.all()
    return render(request,'myapp/services.html',{'courses':courses})

