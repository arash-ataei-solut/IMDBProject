from django.http import JsonResponse
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return JsonResponse({'status': 'you logged out'})
