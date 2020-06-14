from django.shortcuts import render
from django.http import HttpResponse # for using Httpresponse
from .models import Post # for getting data from Post database


def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})   


