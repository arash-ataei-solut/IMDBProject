from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from movie.models.movie import Movie
from movie.models.review import Review
from movie.tasks.send_email import send_email


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
