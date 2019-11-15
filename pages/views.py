from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def rss(request):
    return render(request, 'rss.xml')
