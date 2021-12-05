from django.contrib.auth import authenticate, login,logout
from django.db.transaction import commit
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app_blog.forms import blog_form, loginform,profileinfoform
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
 
def index(req):
    dic= {'name1':'HAPPY','name2':'MILLIONS!!'}
    return render (req, 'app_blog/index.html', dic)

def about(req):
    return render(req, 'app_blog/about.html')

def post(req):
    form = blog_form()
    if req.method == 'POST':
        form= blog_form(req.POST)

        if form.is_valid():
            form.save(commit=True)          
            # print("validation success!!")
            # print(form.cleaned_data['title'])
            # print(form.cleaned_data['blogs'])
            return index(req)
    return render(req, 'app_blog/post.html', {'form':form})

def register(req): 
    registered= False
    if req.method == "POST":
        userform = loginform(data=req.POST)
        profileform = profileinfoform(data= req.POST)
       
        if userform.is_valid() and profileinfoform.is_valid:
           user = userform.save()
           user.set_password(user.password)
           user.save()
           
           profile = profileform.save(commit=False)
           profile.user = user

           if 'profile_pic' in req.FILES:
               profile.profile_pic = req.FILES['profile_pic']
               profile.save()
               registered= True
        else:
            print(userform.errors,profileform.errors)

    else:
        userform = loginform()
        profileform= profileinfoform()        
    return render(req, 'app_blog/register.html',{'userform':userform,'profileform':profileform, 'registered':registered})

@login_required
def special(req):
    return HttpResponse("already logged in!")

@login_required
def logoutview(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))


def loginpageview(req):
    if req.method =="POST": 
        username= req.POST.get('username')
        password = req.POST.get('password')
        user= authenticate(username= username, password= password)
        if user: 
            if user.is_active:
                login(req,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("not logged in")

        else:
            print("failed to login!")
            print("Username:{}, password :{}".format(username, password))
            return HttpResponse("invalid user")

    else:
      return render(req, 'app_blog/login.html',{})

