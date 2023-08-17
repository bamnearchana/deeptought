from django.db import models

# Create your models here.
class Event(models.Model):
    type = models.CharField(default="event", max_length=100)
    uid = models.IntegerField()
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    description = models.TextField()
    files = models.JSONField()
    moderator = models.IntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    rigor_rank = models.IntegerField()
    attendees = models.JSONField()