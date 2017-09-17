from django.db import models

class ContactMessages(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date d'envoi")
    
    def __str__(self):
        return self.subject