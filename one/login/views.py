from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import login
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def register(request):
    return render(request, 'home.html')

def details(request):
    cl = request.POST['class']
    sec = request.POST['section']
    #u = login(username=cl,password=sec).save()
    posts = login.objects.all()
    flag=0
    for post in posts:
        if(post.username == cl and post.password == sec):
            flag=1
    if(flag==1):
        return render(request, 'result.html', {'result': cl})
    else:
        return render(request, 'home.html', {'result': 'Invalid password'})
