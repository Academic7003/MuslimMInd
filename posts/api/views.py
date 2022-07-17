from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.models import PostModel, Creator
from posts.api.serializer import PostSerializer
from rest_framework import filters, viewsets
import django_filters
from rest_framework import status

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icotains')
    body = django_filters.CharFilter(lookup_expr='icotains')

    class Meta:
        model = PostModel
        fields = ['title', 'body']


# @api_view(['GET'])
class ApiPostsListView(viewsets.ViewSet):
    serializer_class = PostSerializer
    queryset=PostModel.objects.all()

    def list(self, request):
        queryset=PostModel.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset=PostModel.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        obj.sees = obj.sees + 1
        obj.save(update_fields=("sees", ))
        serializer = PostSerializer(obj)
        return Response(serializer.data)
        
        

class SearchListView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'body']




@api_view(['GET'])
def post_detail_api_view(request, pk):  
    posts = get_object_or_404(PostModel, pk = pk)
    serializer = PostSerializer(posts)
  
    return Response(serializer.data)

@api_view(['GET'])
def sort_by_creators(request, pk):
    posts = PostModel.objects.filter(creators_id=pk)
    serializer = PostSerializer(posts)
    return Response(serializer.data)


@api_view(['GET'])
def creator_detail_api_view(request, pk):
    posts = get_object_or_404(Creator, pk = pk)
    serializer = Creator(posts)
    return Response(serializer.data)

@api_view(['GET'])
def is_top_view(request):
    posts = PostModel.objects.filter(is_top=True)
    serializer = PostSerializer(posts)
    return Response(serializer.data)


def api_post_downloaded(request, pk):
    file = PostModel.objects.get(pk=pk)
    file.downloads += 1
    file.save()
    return HttpResponse("chotki")



