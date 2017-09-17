from django.conf.urls import url
from usersRanking import views

urlpatterns = [
    url(r'^classement/$', views.ranking),
]