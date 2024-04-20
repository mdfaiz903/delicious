from . models import ContactModel,Feedback
from django import forms 
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'subject', 'msg', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'msg': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'cols': '30', 'rows': '10'}),
        }





# class recipe_blogForm(forms.ModelForm):
#     pic = forms.FileField(widget = forms.TextInput(attrs={"name": "images","type": "File","class": "form-control","multiple": "True",}), label = "")
#     class Meta:
#         model = recipe_blog
#         fields =('title', 'prepaired_time', 'coock_time', 'Servings_person', 'description','pic', )

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             'prepaired_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preparation Time'}),
#             'coock_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cooking Time'}),
#             'Servings_person': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Servings total person'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': '4'}),
          

            
#         }



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message', 'rating' )