from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class BoastOrRoast(models.Model):
    description = models.CharField(max_length=240)
    is_boast = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(default=datetime.now)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    vote_score = models.IntegerField(default=0)