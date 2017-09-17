from django.conf.urls import url
from userMembers import views

urlpatterns = [
    url(r'^inscription/$', views.inscription, name = "inscription"),
    url(r'^connexion/$', views.connexion, name = "connexion"),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^profil/$', views.profil, name='profil'),
]