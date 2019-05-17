from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    movie_id = models.IntegerField(blank=True)
    title = models.TextField(blank=True)
    vote_average = models.FloatField(blank=True)
    popularity = models.FloatField(blank=True)
    poster_path = models.TextField(blank=True)
    original_language = models.TextField(blank=True)
    original_title = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    release_date = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True)
    backdrop_path = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_img = models.TextField()
    score = models.IntegerField()
    content = models.CharField(max_length=140)
    
    def __str__(self):
        return self.content