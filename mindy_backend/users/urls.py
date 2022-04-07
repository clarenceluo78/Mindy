from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
    path('login/', login),
    path('register', register),
    path('logout/', logout),
    path('confirm/', user_confirm),
]