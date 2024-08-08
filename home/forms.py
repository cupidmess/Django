# forms.py
from django import forms

class ContactForm(forms.Form):
    # Define your form fields here
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    email = forms.EmailField()
    web = forms.URLField()
    message = forms.CharField(widget=forms.Textarea)
