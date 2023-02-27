from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('rules/',rules,name='rule'),
    path('posts/',posts,name='posts'),
]