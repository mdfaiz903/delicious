from django.shortcuts import render,HttpResponse
from . models import sliderModel,BlogPost,BlogCategory,ReceipePost,ReceipeImage,RecipeContentSection,Ingredient
from . forms import ContactForm,FeedbackForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q 
# Create your views here.
def searchView(request):
    if request.method=='POST':
        search_input = request.POST.get('search','')
        if search_input:
            result = ReceipePost.objects.filter(
                (Q(title__icontains=search_input)) | (Q(content__post_set__icontains=search_input))
            ).distinct()
        else:
            result = []
            return HttpResponse("<h1>No search input provided.</h1>")


        context={
            'result':result
        } 
    return render(request,'post/search.html',context)

def homeview(request):
    slider = sliderModel.objects.all().order_by('-id')[:3]
    feature = ReceipePost.objects.filter(featured_item=True)
    all_receipe = ReceipePost.objects.all().order_by('-id')
    context = {
        'slider':slider,
        'all_receipe': all_receipe,
        'feature_data': feature,

    }
    return render(request,'delicious/index.html',context)


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




# def recipe_blog_create(request):
#     if request.method == 'POST':
#         post_form = recipe_blogForm(request.POST, request.FILES)
#         if post_form.is_valid():
#             post = post_form.save()
#             for img in request.FILES.getlist('pic'):
#                 post.image_set.create(pic=img)
#             return redirect('home')
#     else:
#         post_form = recipe_blogForm()
#     context = {
#         'post_form':post_form,
        
#     }
#     return render(request, 'delicious/receipe_create.html',context)

def receipeView(request):
    
    receipePost = ReceipePost.objects.all()
    receipeImg = ReceipeImage.objects.all()
    receipeContent = RecipeContentSection.objects.all()
    indData = Ingredient.objects.all()
    context = {
       'rec_post':receipePost,
       'rec_img':receipeImg,
       'rec_cont':receipeContent,
       'rec_intd':indData,
   }
    return render(request,'delicious/receipe-post.html',context)

def receipeViewdetails(request, id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            rating = form.cleaned_data['rating']
            # You can print these values to debug
            print("Message:", message)
            print("Rating:", rating)
            print("POST Data:", request.POST)  # Print entire POST data for debugging
            # form.save()
            messages.success(request, "Feedback Submitted")
            return HttpResponse("Form submitted successfully!") 
    else:
        form = FeedbackForm()
    
    receipePost = ReceipePost.objects.get(id=id)

    context = {
        'receipePost': receipePost,
        'form': form,
    }
    return render(request, 'delicious/receipe-details.html', context)

# def receipeViewdetails(request, id):
#     receipePost = get_object_or_404(ReceipePost,id=id)
#     if request.method=='POST':
#         msg = request.POST.get('message')
#         rating = request.POST.get('rating')
#         print("Message:", msg)
#         print("Rating:", rating)
#         print(request.POST)
#         # form = FeedbackForm(request.POST)
#         # if form.is_valid():
         
          
#         #     form.rating = int(request.POST.get('rating'))  # Get rating from POST data
#         #     print(form.rating,'++++++++++++')
#         #     # feedback.save()  # Save now with the updated rating
#         #     messages.success(request, "Feedback Submitted")
#     # else:
#         # form = FeedbackForm()

#     context = {
#         'receipePost': receipePost,
#         # 'form': form,
#     }
#     return render(request, 'delicious/receipe-details.html', context)
def contactView(request):
    return render(request,'delicious/contact.html')

