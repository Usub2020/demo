from django import forms
from polls.models import *

class contactform (forms.ModelForm):
    name = forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))
    email = forms.EmailField(max_length=250,required=True,widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    phone =forms.CharField( max_length=50,required=True,help_text='Contact phone number',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone number'
    }))

    subject = forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'subject'
    }))
    # pip install django-widget-tweaks
    #  instaled setting app 'widget_tweaks',
    # {% load widget_tweaks %}
    # <!-- add 2 extra css classes to field element -->
    # {{ form.title|add_class:"css_class_1 css_class_2" }}

    
    mesage = forms.CharField(max_length=1500,required=True,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message'
    }))

    def clean(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        subject = self.cleaned_data.get('subject')
        mesage = self.cleaned_data.get('mesage')

    # def __init__(self, *args, **kwargs):
    #     super(contactform, self).__init__(*args, **kwargs)
    #     self.fields['subject'].widget.attrs.update({'class': 'form-control','style':'color:black;'})

    class Meta :
        model = contact
        fields = ['name','email','phone','subject','mesage']
