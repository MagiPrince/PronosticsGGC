from django.shortcuts import render
from django.apps import apps

def ranking(request):
	profil = apps.get_model("userMembers", "Profil")

	listRanking = profil.objects.order_by("-nbGGCPoints")

	return render(request, "usersRanking/ranking.html", {"listRanking" : listRanking})