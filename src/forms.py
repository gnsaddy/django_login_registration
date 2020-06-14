from django import forms


class Contactus(forms.Form):
    yourname = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(label="Email", max_length=100, required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Email Id'
    }))
    subject = forms.CharField(max_length=300, label="Subject", widget=forms.TextInput(attrs={
        'class': 'form-control rounded-pill',
        'placeholder': 'Enter subject'
    }))
    msg = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter message...'
    }))
