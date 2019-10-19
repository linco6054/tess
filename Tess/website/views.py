from django.shortcuts import render
from django.http import HttpResponse , Http404
from django.template import loader
from . models import Card


def index(request):
    context={
        'card': Card.objects.all()
    }
    return render(request, 'website/index.html', context)
def about(request):
    return render(request,'website/about.html')
def newsletter(request):
    return render(request, 'website/newsletter.html')
def audio_video(request):
    return render(request, 'website/audio_video.html')


def book_session(request):
    return render(request, 'website/book_session.html')

