from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')
