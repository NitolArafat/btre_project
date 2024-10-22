from django.contrib.auth.models import User
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib import messages,auth
from contacts.models import Contacts
from django.http import HttpResponse


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        # Check if password match

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This email is being used')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    #auth.login(request,user)
                    # messages.success(request,'You are logged in')
                    # return  redirect('index')
                    user.save()
                    messages.success(request, 'You are logged in')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')


        #messages.error(request, 'Testing error message')
        # Register users
        return redirect('register')
    else:
        return render(request,'accounts/register.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #meytext = request.POST['meytext']
        # if password == '':
        #     return HttpResponse('tor heda')
        # else:
        #     return HttpResponse('th')
        user= auth.authenticate(username=username, password=password)
        #return HttpResponse(user)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
        return redirect('login')


        # print('login')
    else:
        return render(request,'accounts/login.html')



def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,'You are now logged out')

    return redirect('index')




def dashboard(request):
    user_contact=Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contact
    }
    return render(request, 'accounts/dashboard.html',context)
