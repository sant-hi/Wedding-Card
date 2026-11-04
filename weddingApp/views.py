from django.shortcuts import render,redirect
from weddingApp.models import *
from django.shortcuts import render

from .models import (
    WeddingProfile,
    GalleryImage,
)


def index(request):
    profile = WeddingProfile.objects.first()
    gallery_images = GalleryImage.objects.all()
    context = {
        'profile': profile,
        'gallery_images': gallery_images,
    }
    return render(
        request,
        'index.html',
        context
    )






# Create your views here.
