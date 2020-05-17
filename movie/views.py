from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Movie, Rate, Review
from .tasks import send_email


def movies_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        response = []
        for movie in movies:
            movie_data = movie.__dict__
            del movie_data['_state']
            response.append(movie_data)
        return JsonResponse({'results': response})


def movies_retrieve_view(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.filter(
            pk=pk
        ).prefetch_related(
            'rates', 'reviews'
        ).annotate(
            average_rate=Avg('rates__rate')
        )
        if movie:
            movie_data = movie[0].__dict__
            for i in movie_data['_prefetched_objects_cache'].keys():
                poi = []
                for j in movie_data['_prefetched_objects_cache'][i]:
                    poi_data = j.__dict__
                    del poi_data['_state']
                    poi.append(poi_data)
                movie_data[i] = poi
            del movie_data['_state']
            del movie_data['_prefetched_objects_cache']
            return JsonResponse(movie_data)
        else:
            return JsonResponse({'error': 'the movie was not found'}, status=404)
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)


@login_required
def rate_view(request, pk):
    if request.method == 'POST':
        rate = request.POST.get('rate')
        user = request.user
        movie = get_object_or_404(Movie, pk=pk)
        Rate.objects.get_or_create(rate=rate, user=user, movie=movie)
        return JsonResponse({'rate': rate}, status=200)
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)


@login_required
def review_view(request, pk):
    if request.method == 'POST':
        text = request.POST.get('text')
        user = request.user
        movie = get_object_or_404(Movie, pk=pk)
        Review.objects.create(text=text, user=user, movie=movie)
        send_email.delay(user.id, movie.id, text)
        return JsonResponse({'text': text}, status=200)
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
