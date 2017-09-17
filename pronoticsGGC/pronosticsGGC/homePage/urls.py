from django.conf.urls import url
from homePage import views

urlpatterns = [
    url(r'^$', views.home),
]