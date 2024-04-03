from django.shortcuts import render
from . models import sliderModel
# Create your views here.


def homeview(request):
    slider = sliderModel.objects.all().order_by('-id')[:3]
    return render(request,'delicious/index.html',{'slider':slider})


def aboutView(request):
    return render(request,'delicious/about.html')
def blogView(request):
    return render(request,'delicious/blog-post.html')
def receipeView(request):
    return render(request,'delicious/receipe-post.html')
def contactView(request):
    return render(request,'delicious/contact.html')

