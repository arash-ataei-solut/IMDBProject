from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from movie.models.rate import Rate
from movie.models.movie import Movie


@login_required
def rate_view(request, pk):
    if request.method == 'POST':
        rate = request.POST.get('rate')
        user = request.user
        movie = get_object_or_404(Movie, pk=pk)
        Rate.objects.get_or_create(rate=rate, user=user, movie=movie)
        return JsonResponse({'rate': rate}, status=200)
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
