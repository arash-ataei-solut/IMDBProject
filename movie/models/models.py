from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    languages = [
        ('EN', 'English'),
        ('FA', 'Persian'),
        ('ES', 'Spanish'),
        ('HI', 'Hindi'),
        ('IT', 'Italian')
    ]

    name = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    language = models.CharField(max_length=255, choices=languages)


class Rate(models.Model):
    rate = models.DecimalField(max_digits=2, decimal_places=2, default=0.99, help_text=_('A number between 0 and 1'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rates')

    class Meta:
        unique_together = ('user', 'movie')


class Review(models.Model):
    text = models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
