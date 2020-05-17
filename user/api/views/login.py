from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'you logged in successfully.'})
        else:
            return JsonResponse({'status': 'wrong username or password'})
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
