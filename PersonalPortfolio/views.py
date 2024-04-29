from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'HomePage.html')

def projects(request):
    return render(request, "Projects.html")
