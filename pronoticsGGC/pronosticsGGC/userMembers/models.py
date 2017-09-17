from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profil(models.Model):
	user = models.OneToOneField(User)
	nbGGCPoints = models.IntegerField(default = 0)
	nbVotes = models.IntegerField(default = 0)
	ratio = models.IntegerField(default = 100)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profil(sender, instance, **kwargs):
    instance.profil.save()
