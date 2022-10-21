from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField

class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField
    likes = models.IntegerField
    artiste_id = models.IntegerField

class Lyric(models.Model):
    content = models.CharField
    song_id = models.IntegerField