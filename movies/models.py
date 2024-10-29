from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=80)
    
class Person(models.Model):
    name = models.CharField(max_length=80)
    
class Job(models.Model):
    name = models.CharField(max_length=30)
    
Class Movie(models.Model):
    title =  models.CharField(max_length=200)
    overview =  models.TextField()
    release_date = models.DateField()
    running_time = models.IntegerField()
    budget =  models.IntegerField(blank=true)
    tmdb_id = models.IntegerField(blank=true)
    revenue = models.IntegerField(blank=true)
    poster_patch = models.URLField(blank=true)
    genres = models.ManyToManyField(Genre)
    credits = models.ManyToManyField(Person, through='MovieCredit')
    
    Class MovieCredit(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)