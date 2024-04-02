from django.shortcuts import render

# Create your views here.


def homeview(request):
    return render(request,'delicious/index.html')


def aboutView(request):
    return render(request,'delicious/about.html')
def blogView(request):
    return render(request,'delicious/blog-post.html')
def receipeView(request):
    return render(request,'delicious/receipe-post.html')
def contactView(request):
    return render(request,'delicious/contact.html')

