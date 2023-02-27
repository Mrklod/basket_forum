from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('rules/',rules,name='rule'),
    path('posts/',posts,name='posts'),
    path('posti/<int:post_id>',single_post,name='single_post'),
    path('add_post/',add_post,name='add_post')
]