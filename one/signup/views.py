from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import sign,details
def register(request):
    return render(request, 'register.html')

def signup(request):
    cl = request.POST['username']
    sec = request.POST['password']
    u = sign(username=cl,password=sec).save()
    return render(request, 'result.html', {'result': cl})

def login(request):
    cl = request.POST['user']
    sec = request.POST['pass']
    posts = sign.objects.all()
    flag = 0
    for post in posts:
        if (post.username == cl and post.password == sec):
            flag = 1
    if (flag == 1):
        return render(request, 'result.html', {'result': cl})
    else:
        return render(request, 'register.html', {'result': 'Invalid password'})


def adduser(request):
    return render(request, 'student_details.html')

def stud_details(request):
    name = request.POST['name']
    clas = request.POST['class']
    email = request.POST['email']
    phone = request.POST['phone']
    u = details(name=name, clas=clas, email=email, phone=phone).save()
    return render(request, 'result.html')

def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response
def getcookie(request):
    tutorial  = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: "+  tutorial);