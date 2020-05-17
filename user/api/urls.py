from django.urls import path

from user.api.views.login import login_view
from user.api.views.logout import logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
