from django.shortcuts import render, get_list_or_404
from django.views.generic import TemplateView
from posts.models import *


class Test(TemplateView):
    template_name = 'index.html'



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
