from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'christmas/index.html')

def about(request):
    return render(request, 'christmas/about.html')

def recipes(request):
    return render(request, 'christmas/recipes.html')