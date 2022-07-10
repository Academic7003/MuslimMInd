from django.urls import path
from posts.views import *

app_name = 'posts'

urlpatterns = [
    path('', view_posts, name='main'),
    path('detail/<int:pk>', detail_post, name='detail'),
    path('post-downloaded/<int:pk>', post_downloaded, name="download"),
    path('post-seed/<int:pk>', post_seed, name="sees"),
    path('creatordetail/<int:pk>', sort_by_creator, name='creatordetail')
    
]
