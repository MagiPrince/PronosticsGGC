from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from smart_selects.db_fields import ChainedForeignKey


class GameName(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class TeamGGC(models.Model):
	teamName = models.CharField(max_length = 100)
	stillInCompetition = models.BooleanField(default = True)
	teamGame = models.ForeignKey("GameName")

	def __str__(self):
		return self.teamName

class MatchOpponents(models.Model):
	gameName = models.ForeignKey("GameName")
	matchName = models.CharField(max_length = 100)
	equipeOne = ChainedForeignKey(
        TeamGGC,
        chained_field="gameName", 
        chained_model_field="teamGame",
        show_all=False,
        related_name="equipeOne"
    )
	equipeTwo = ChainedForeignKey(
        TeamGGC,
        chained_field="gameName",
        chained_model_field="teamGame",
        show_all=False,
        related_name="equipeTwo"
    )
	matchStarting = models.DateTimeField()

	def __str__(self):
		return self.matchName

class Prognostic(models.Model):
	match = models.ForeignKey("MatchOpponents")
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	vote = models.ForeignKey("TeamGGC")

	def __int__(self):
		return self.vote

class MatchResult(models.Model):
	matchNumber = models.ForeignKey("MatchOpponents")
	gameName = models.ForeignKey("GameName")
	winner = ChainedForeignKey(
        TeamGGC,
        chained_field="gameName",
        chained_model_field="teamGame",
        show_all=False,
        related_name = "winner"
    )

	def __int__(self):
		return self.match
