from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location, Category


def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Urban Gallery'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})