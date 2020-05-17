from django.urls import path

from movie.api.views.movies_list import movies_list_view
from movie.api.views.movies_retrieve import movies_retrieve_view
from movie.api.views.rate import rate_view
from movie.api.views.review import review_view

urlpatterns = [
    path('movies/', movies_list_view, name='movies'),
    path('movies/<int:pk>/', movies_retrieve_view, name='movie'),
    path('rate/<int:pk>/', rate_view, name='rate'),
    path('review/<int:pk>/', review_view, name='review')
]
