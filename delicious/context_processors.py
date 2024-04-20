from delicious . models import sliderModel
from . forms import ContactForm
from django.shortcuts import HttpResponse,get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
def sld_context (request):
    sld = sliderModel.objects.all().order_by('-id')[:2]
    return {'slider':sld}


def ContactView(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
         
            current_site = get_current_site(request)
            mail_subject = "Message Submission"
            message = render_to_string('../templates/commonFiles/msg_temp.html',{
                'user':request.user.username,
                'domain':current_site.domain,
                
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            messages.info(request,'Form successfully sent, Please check your Mail box')
           
            
    else:
        form = ContactForm()
    return {'form':form}


