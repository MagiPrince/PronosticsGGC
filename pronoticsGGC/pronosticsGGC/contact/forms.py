from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(label="Votre adresse mail", required = True)