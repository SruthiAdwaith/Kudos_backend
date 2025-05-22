from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)

class Kudos(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_kudos')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_kudos')
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


