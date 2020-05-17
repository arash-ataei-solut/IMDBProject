from django.urls import path

from movie.api.views.views import movies_list_view, movies_retrieve_view, rate_view, review_view

urlpatterns = [
    path('movies/', movies_list_view, name='movies'),
    path('movies/<int:pk>/', movies_retrieve_view, name='movie'),
    path('rate/<int:pk>/', rate_view, name='rate'),
    path('review/<int:pk>/', review_view, name='review')
]
