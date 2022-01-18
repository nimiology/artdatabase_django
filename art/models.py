from django.db import models


class Art(models.Model):
    artist = models.CharField(max_length=2048)
    title = models.CharField(max_length=2048)
    picture = models.URLField()
    year = models.CharField(max_length=100)
    type = models.CharField(max_length=2048)
    location = models.CharField(max_length=2048)
