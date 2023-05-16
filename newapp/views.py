from django.shortcuts import render,redirect
from django.http import HttpResponse
from. admin import *

# Create your views here.
def log(request):
    return render(request,'log.html')
def reg(request):
    return render(request,'reg.html')
def reg1(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        a = Register(username=username,email=email,password1=password1,password2=password2)
        a.save()
        b = Login(username=username,password1=password1,type=1)
        b.save()
        return render(request,'reg.html')
def valid(request):
    username = request.POST['username']
    password1 = request.POST['password1']
    c=Login.objects.get(username=username,password1=password1)
    if c.type==1:
        request.session['username']=c.username
        return render(request,'index.html')
    if c.type==0:
        request.session['password1']=c.password1
        return render(request,'adhome.html')

def home(request):
    return render(request, 'index.html')
def adhome(request):
    return render(request, 'adhome.html')
def about(request):
    return render(request, 'about.html')
def home1(request):
    return render(request, 'index.html')
def serform(request):
    if request.method == "POST":
        img = request.POST['img']
        head = request.POST['head']
        data = request.POST['data']
        s=Service(img=img,head=head,data=data)
        s.save()
        return render(request, 'service.html')
def service(request):
    read=Service.objects.all()
    re={'service':read}
    return render(request, 'service.html',re)
def proform(request):
    if request.method == "POST":
        img = request.POST['img']
        head = request.POST['head']
        data = request.POST['data']
        p=Project(img=img,head=head,data=data)
        p.save()
        return render(request, 'project.html')
def project(request):
    red=Project.objects.all()
    rd={'project':red}
    return render(request, 'project.html',rd)
def contact(request):
    return render(request, 'contact.html')

def supdate(request,id):
    if request.method == "POST":
        img = request.POST['img']
        head = request.POST['head']
        data = request.POST['data']
        mn=Service(img=img,head=head,data=data)
        mn.img=img
        mn.head=head
        mn.data=data
        mn.save()
        return redirect("/")
    y=Service.objects.get(id=id)
    q={"r":y}
    return render(request,"supdate.html",q)
def service1(request):
    read = Service.objects.all()
    re = {'service': read}
    return render(request, 'service1.html',re)

def sde(request,id):
    ed=Service.objects.get(id=id)
    ed.delete()
    return redirect(service1)

def pupdate(request,id):
    if request.method == "POST":
        img = request.POST['img']
        head = request.POST['head']
        data = request.POST['data']
        jk= Project(img=img,head=head,data=data)
        jk.img = img
        jk.head = head
        jk.data = data
        jk.save()
        return redirect("/")
    z = Project.objects.get(id=id)
    k = {"j": z}
    return render(request, "pupdate.html", k)

def project1(request):
    red=Project.objects.all()
    rd={'project':red}
    return render(request, 'project1.html',rd)

def prd(request,id):
    rd=Project.objects.get(id=id)
    rd.delete()
    return redirect(project1)

def newabt(request):
    return render(request,'newabout.html')