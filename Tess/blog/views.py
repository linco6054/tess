from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Admin_Post
# Create your views here.


def index(request):
    context ={
        'posts': Admin_Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def login(request):
    return render(request, 'blog/login.html', )
