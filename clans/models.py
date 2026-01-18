from django.db import models

# Create your models here.

class Clans(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    team_size = models.IntegerField()
    