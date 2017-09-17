from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessages


def contact(request):

	form = ContactForm(request.POST or None)
	contactData = ContactMessages()

	if form.is_valid(): 

		subject = form.cleaned_data['subject']
		content = form.cleaned_data['content']
		email = form.cleaned_data['email']

		envoi = True

		messages.info(request,'Le formulaire a été envoyé !')
		contactData.subject = subject
		contactData.content = content
		contactData.email = email

		contactData.save()

	return render(request, 'contact/contactForm.html', locals())