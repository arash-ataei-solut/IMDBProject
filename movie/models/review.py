from django.contrib.auth.models import User
from django.db import models

from movie.models.movie import Movie


class Review(models.Model):
    text = models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
