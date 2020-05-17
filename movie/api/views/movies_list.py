from django.http import JsonResponse

from movie.models.movie import Movie


def movies_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        response = []
        for movie in movies:
            movie_data = movie.__dict__
            del movie_data['_state']
            response.append(movie_data)
        return JsonResponse({'results': response}, status=200)
