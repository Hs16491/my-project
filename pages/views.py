from django.shortcuts import render
from .models import Login
from .forms import LoginForms
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
    if request.method == 'POST':
        dataform = LoginForms(request.POST)
        if dataform.is_valid():
            dataform.save()
        else:
            form = LoginForms()
    
    
    
    #if request.method == 'POST':
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        #data = Login(username=username, password=password)
        #data.save()

    return render(request, 'pages/login.html', {'lform': LoginForms()})