from django.shortcuts import render
from .models import Profil
from .forms import RegistrationForm
from .forms import ConnexionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.apps import apps

def inscription(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            envoi = True
            return render(request, "userMembers/inscription.html", locals())
        else:
            return render(request, "userMembers/inscription.html", locals())
    else:
        form = RegistrationForm()
        args = {"form": form}
        return render(request, "userMembers/inscription.html", args)

def update_profil(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profil.nbGGCPoints = 0
    user.save()

    return render(request, "userMembers/inscription.html", locals())

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect("/")
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'userMembers/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def profil(request):

    votes = apps.get_model("tournamentGames", "Prognostic")
    user = request.user.id

    listVotes = votes.objects.filter(user_id = user)


    return render(request, "userMembers/profil.html", {"listVotes": listVotes})
