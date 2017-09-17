from django.contrib import admin
from .models import TeamGGC, GameName, MatchOpponents, Prognostic, MatchResult
from django.apps import apps
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class PrognosticInLine(admin.TabularInline):
	model = Prognostic

class MatchResultInLine(admin.TabularInline):
	model = MatchResult


class MatchOpponentsAdmin(admin.ModelAdmin):
	inlines = [PrognosticInLine, MatchResultInLine]

	def matchMAJ(modeladmin, request, queryset):
		profil = apps.get_model("userMembers", "Profil")
		for match in MatchResult.objects.all():
			prognostic = Prognostic.objects.filter(vote = match.winner)
			for prog in prognostic:
				p = profil.objects.filter(user_id = prog.user.pk)
				for userProfil in p:
					userProfil.nbGGCPoints += 50;
					userProfil.save()
				for user in prog.user:
					if user.nbVotes >= 1:
						user.ratio = (prof.nbGGCPoints/50)/prof.nbVotes*100
						user.save()

		for match in MatchResult.objects.all():
			for prog in Prognostic.objects.filter(match_id = match.matchNumber):
				for prof in profil.objects.filter(user_id = prog.user):
					prof.ratio = (prof.nbGGCPoints/50)/prof.nbVotes*100
					prof.save()
				prog.delete()
			


class MatchResultAdmin(admin.ModelAdmin):
	actions = ["MAJ"]

	def MAJ(modeladmin, request, queryset):
		MatchOpponentsAdmin.matchMAJ(modeladmin, request, queryset)
		


admin.site.register(TeamGGC)
admin.site.register(GameName)
admin.site.register(MatchOpponents)
admin.site.register(Prognostic)
admin.site.register(MatchResult, MatchResultAdmin)