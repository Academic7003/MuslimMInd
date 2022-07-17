from django.urls import path, include
from posts.api.views import *

urlpatterns = [
    path('', ApiPostsListView.as_view({'get':'list'})),
    path('posts/<int:pk>', ApiPostsListView.as_view({'get':'retrieve'})),
    path('search/', SearchListView.as_view()),
    
    path('author-posts/<int:pk>', sort_by_creators),
    path('author-detail/<int:pk>', creator_detail_api_view),
    path('tops/', is_top_view),
    path('post-downloaded/<int:pk>', api_post_downloaded),







]
