from django.db.models import Avg
from django.http import JsonResponse

from movie.models.movie import Movie


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
            return JsonResponse(movie_data, status=200)
        else:
            return JsonResponse({'error': 'the movie was not found'}, status=404)
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
