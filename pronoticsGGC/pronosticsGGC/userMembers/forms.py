from django import forms
from django.contrib.auth.models import User
from .models import Profil
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):


	email = forms.EmailField(required = True)
	username = forms.CharField(label = "Nom d'utilisateur ", required = True, help_text=("Les lettres, chiffres et @/./+/-/ sont autorisés"))
	first_name = forms.CharField(label = "Prénom ", required = True)
	last_name = forms.CharField(label = "Nom ", required = True)
	email = forms.CharField(label = "Email ")
	password1 = forms.CharField(label = "Mot de passe ", required = True, widget = forms.PasswordInput)
	password2 = forms.CharField(label = "Vérifier le mot de passe ", required = True, widget=forms.PasswordInput,
        help_text=("Retapez votre mot de passe"))
	checkBox = forms.BooleanField(label = "J'accepte les termes et conditions d'utilisation ", required = True)

	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name",
			"email",
			"password1",
			"password2"
			)

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exists():
			 raise forms.ValidationError("Cet email est déjà utilisé !")
		return email

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit = False)
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.email = self.cleaned_data["email"]

		if commit:
			user.save()

		return user


class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)