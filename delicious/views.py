from django.shortcuts import render
from . models import sliderModel,BlogPost,BlogCategory
from . forms import ContactForm

# Create your views here.


def homeview(request):
    slider = sliderModel.objects.all().order_by('-id')[:3]
    return render(request,'delicious/index.html',{'slider':slider})


def ContactView(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render(request,'delicious/receipe-post.html',{'form':form})





def aboutView(request):


    return render(request,'delicious/about.html')
def blogView(request):
    queryset = BlogPost.objects.all()
    blog_item = BlogCategory.objects.all()

    context = {
        'items':queryset,
        'blog_items':blog_item
    }
    return render(request,'delicious/blog-post.html',context)
def blog_details(request,id):
    post = BlogPost.objects.get(id=id)

    return render(request,'delicious/blog-details.html',{'post':post})
def receipeView(request):
    return render(request,'delicious/receipe-post.html')
def contactView(request):
    return render(request,'delicious/contact.html')

