from . models import ContactModel
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