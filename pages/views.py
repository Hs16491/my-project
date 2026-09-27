from django.shortcuts import render
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