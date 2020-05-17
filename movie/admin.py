from django.contrib import admin
from movie.models.models import Movie, Rate, Review


admin.site.register(Movie)
admin.site.register(Rate)
admin.site.register(Review)
