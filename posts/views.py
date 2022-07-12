from django.shortcuts import render, get_list_or_404, get_object_or_404
from posts.models import *
from django.http import HttpResponse
from django.db.models import Q 
from creators.models import Creator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def view_posts(request):
    context = {}
    posts_list = PostModel.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {'posts': posts}
    # pois
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
    # random post
    r_posts = PostModel.objects.order_by('?')
    try:
        r_posts = r_posts[:6]
    except:
        r_posts = r_posts
    context['r_posts'] = r_posts
    # is top
    tops = PostModel.objects.filter(is_top =True)
    try:
        tops = tops[:6]
    except:
        tops = tops
    context['tops'] = tops
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

    
