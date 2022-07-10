from django.shortcuts import render, get_list_or_404, get_object_or_404
from posts.models import *
from django.http import HttpResponse
from django.db.models import Q 
from creators.models import Creator



def view_posts(request):
    context = {}
    posts = PostModel.objects.all()
    context['posts'] = posts
    query = request.GET.get('q','')
    #The empty string handles an empty "request"
    if query:
        # queryset = (Q(barcode__icontains=query))
        #I assume "text" is a field in your model
        #i.e., text = model.TextField()
        #Use | if searching multiple fields, i.e., 
        queryset = (Q(title__icontains=query))
        result = PostModel.objects.filter(queryset).distinct()

    else:
       result = []
    context['result'] = result
    context['query']=query
    return render(request, 'main.html', context)

def detail_post(request, pk):
    context = {}
    post = get_list_or_404(PostModel, pk=pk)
    context['post'] = post
    return render(request, 'detail.html', context)


def post_downloaded(request, pk):
    context = {}
    file = PostModel.objects.get(pk=pk)
    file.downloads += 1
    file.save()
    return render(request, 'detail.html', context)

def post_seed(request, pk):
    context = {}
    file = PostModel.objects.get(pk=pk)
    file.sees += 1
    file.save()
    return render(request, 'detail.html', context)
    
def sort_by_creator(request, pk):
    context = {}

    posts = PostModel.objects.filter(creators_id=pk)
    creator = get_object_or_404(Creator, pk=pk)
    context['posts'] = posts
    context['creator'] = creator
    return render(request, 'creatordetail.html', context)