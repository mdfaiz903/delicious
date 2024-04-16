from django.shortcuts import render
from . models import sliderModel,BlogPost,BlogCategory
from . forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    queryset = BlogPost.objects.all().order_by('-id')
    blog_item = BlogCategory.objects.all()
    paginator = Paginator(queryset,3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'items':queryset,
        'blog_items':blog_item,
        'page_obj':page_obj,
    }
    return render(request,'delicious/blog-post.html',context)
def blog_details(request,id):
    post = BlogPost.objects.get(id=id)

    return render(request,'delicious/blog-details.html',{'post':post})
def receipeView(request):
    return render(request,'delicious/receipe-post.html')
def contactView(request):
    return render(request,'delicious/contact.html')

