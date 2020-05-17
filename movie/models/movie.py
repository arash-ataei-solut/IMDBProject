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
