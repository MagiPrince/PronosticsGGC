from django.conf.urls import url
from tournamentGames import views

urlpatterns = [
    url(r'^matchs/([a-zA-Z\s]+)$', views.displayMatchs, name = "dispayMatchs"),
    url(r'^match/(\d+)$', views.infosMatch, name='infosMatch'),
    url(r'^match/$', views.voteTeam),
]