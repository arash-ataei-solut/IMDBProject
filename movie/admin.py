from django.contrib import admin

from movie.models.movie import Movie
from movie.models.rate import Rate
from movie.models.review import Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('name', 'release_date', 'director', 'language')
    list_display = ('name', 'release_date', 'director', 'language')
    list_filter = ('name', 'release_date', 'director', 'language')
    search_fields = ('name', 'release_date', 'director', 'language')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    fields = ('rate', 'user', 'movie')


@admin.register(Review)
class RateAdmin(admin.ModelAdmin):
    fields = ('text', 'user', 'movie')
