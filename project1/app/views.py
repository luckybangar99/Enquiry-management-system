from django.shortcuts import render
from .models import UserDataBase,QueryDataBase,AdminDataBase


def home(req):
    return render(req,"home.html")

def uregis(req):
    return render(req,"uregis.html")

def aregis(req):
    return render(req,"aregis.html")

def users(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        k=UserDataBase.objects.filter(Email=email)
        if pass1!=pass2:
            msg="Password not Match"
            return render(request,'uregis.html',{'msg':msg})
        if k:
            msg=" Invalid Email Id"
            return render(request,'uregis.html',{'msg':msg})
        else:
            D=UserDataBase(Fname=lname,Lname=lname,Contact=contact,Email=email,Password=pass1,Cpass=pass2)
            D.save()
    return render(request,'uregis.html')

def Login(req):
    if req.method=="POST":
        email=req.POST.get('email')
        password=req.POST.get('pass')
        a=UserDataBase.objects.filter(Email=email,Password=password)
        if a:
            return render(req,'udash.html')
        else:
            msg="Password Doesnt Match"
            return render(req,'ulogin.html',{'msg':msg})
    return render(req,'ulogin.html')  

def userdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('cont')
        query=request.POST.get('txt')
        d=QueryDataBase(Name=name,Email=email,Contact=contact,Query=query)
        d.save()
    return render(request,'home.html')


#                          ----------Admin start---------------------

def adminn(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        k=AdminDataBase.objects.filter(Email=email)
        if pass1!=pass2:
            msg="Password not Match"
            return render(request,'aregis.html',{'msg':msg})
        if k:
            msg=" Invalid Email Id"
            return render(request,'aregis.html',{'msg':msg})
        else:
            D=AdminDataBase(Fname=fname,Lname=lname,Contact=contact,Email=email,Password=pass1,Cpass=pass2)
            D.save()
           # return render(request,'ulogin.html')
    return render(request,'aregis.html')

def aLogin(req):
    if req.method=="POST":
        email=req.POST.get('email')
        password=req.POST.get('pass')
        a=AdminDataBase.objects.filter(Email=email,Password=password)
        if a:
            return render(req,'adash.html')
        else:
            msg="Password Doesnt Match"
            return render(req,'alogin.html',{'msg':msg})
    return render(req,'alogin.html')  


def adash(request):
    return render(request,'adash.html')

def Admindatadisplay(request):
    d=AdminDataBase.objects.all()
    return render(request,"adisp.html",{"data":d})


def Userdatadisplay(request):
    d=UserDataBase.objects.all()
    return render(request,"udisp.html",{"data":d})

def Querydatadisplay(request):
    d=QueryDataBase.objects.all()
    return render(request,"datadisp.html",{"data":d})

