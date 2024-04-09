from delicious . models import sliderModel
from . forms import ContactForm
from django.shortcuts import HttpResponse
from django.contrib import messages
def sld_context (request):
    sld = sliderModel.objects.all().order_by('-id')[:2]
    return {'slider':sld}


def ContactView(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Form successfully sent")
            
    else:
        form = ContactForm()
    return {'form':form}


