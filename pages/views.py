from django.shortcuts import render
from .models import Login
#from django.http import HttpResponse
# Create your views here.

def index(request):
    x = {'name':'habiba',
    'age':300000000}
    return render(request, 'pages/index.html', x)
    #pass
    #return HttpResponse('hello world')

def about(request):
     return render(request, 'pages/about.html')

    #pass
    #return HttpResponse('about page') 

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(f"Username: {username}, Password: {password}")
    data = Login.objects.create(username=username, password=password)
    data.save()

    return render(request, 'pages/login.html')