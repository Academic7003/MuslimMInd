from django.urls import path
from posts.views import Test
app_name = 'posts'

urlpatterns = [
    path('', Test.as_view(), name='test')
]
