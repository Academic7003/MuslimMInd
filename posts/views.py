import imp
from django.shortcuts import render, get_list_or_404
from posts.models import *
from django.http import HttpResponse
from posts.forms import SeesForm




def view_posts(request):
    context = {}
    posts = PostModel.objects.all()
    context['posts'] = posts
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
    