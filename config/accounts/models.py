from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    class TypeUtilisateur(models.TextChoices):
        AGENT = "AG", 'Agent'
        AGENCY = "AY", 'Agency'
        USERSIMPLE = "US", 'Usersimple'

    base_TypeUtilisateur = TypeUtilisateur.AGENT

    type_utilisateur = models.CharField(max_length=50, choices=TypeUtilisateur.choices)   
    def save(self, *arg, **kwargs):
        if not self.pk:
            self.type_utilisateur = self.base_TypeUtilisateur
            return super().save(*arg, **kwargs)



    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_no = models.CharField(null=False, max_length=10)
    
