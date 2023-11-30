from django import forms
from django.forms import ModelForm
from applications.book.models import Contact, Subscribe

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email_address', 'subject', 'message')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Enter your full name'})
        self.fields['email_address'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['subject'].widget.attrs.update({'placeholder': 'Enter your subject'})
        self.fields['message'].widget.attrs.update({'placeholder': 'Enter your message', 'type':'text'})
		
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})