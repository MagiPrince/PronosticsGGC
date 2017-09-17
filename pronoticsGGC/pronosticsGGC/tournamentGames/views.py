from django.shortcuts import render, get_object_or_404
from .models import MatchOpponents, Prognostic, MatchResult, GameName
import datetime
from django.http import Http404
from django.contrib.auth.models import User
from django.apps import apps

def displayMatchs(request, gameRef):
	if gameRef == "all":
		matchs = MatchOpponents.objects.filter(matchStarting__gt = datetime.datetime.now()).order_by("matchStarting")
	else:
		gameId = GameName.objects.filter(name = gameRef)
		matchs = MatchOpponents.objects.filter(matchStarting__gt = datetime.datetime.now(), gameName = gameId).order_by("matchStarting")
	typeGames = GameName.objects.all()
	return render(request, "tournamentGames/parier.html", {'next_matchs': matchs, "typeGames": typeGames})

def infosMatch(request, id):
	try:
		match = MatchOpponents.objects.filter(matchStarting__gt = datetime.datetime.now()).get(id=id)
		vote = Prognostic.objects.filter(match_id = id)
		voted = False
		user = request.user.id
		for v in vote:
			if v.user_id == user:
				voted = True
	except MatchOpponents.DoesNotExist:
		raise Http404

	return render(request, 'tournamentGames/infosMatch.html', {'match': match, "vote": vote, "voted": voted})

def voteTeam(request):

	
	prognostic = Prognostic()
	voted = False
	user = request.user.id
	profil = apps.get_model("userMembers", "Profil")
	userProfil = profil.objects.filter(user_id = user)


	if request.method == "POST":
		if "voteTeam" not in request.POST:
			voteTeam = request.POST["voteTeamOpponent"]
		else:
			voteTeam = request.POST["voteTeam"]
		match = int(request.POST["match"])

	vote = Prognostic.objects.filter(match_id = match)

	for v in vote:
		if v.user_id == user:
			voted = True

	if voted == False:

		prognostic.match_id = match
		prognostic.vote_id = voteTeam
		prognostic.user_id = user

		for prof in userProfil:
			prof.nbVotes += 1
			prof.save()

		prognostic.save()

	return render(request, 'tournamentGames/voteOk.html', locals())

