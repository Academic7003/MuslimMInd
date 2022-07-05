from django.urls import path
from posts.views import *

app_name = 'posts'

urlpatterns = [
    path('', view_posts, name='test')
]
