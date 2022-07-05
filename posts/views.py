from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import *


class Test(TemplateView):
    template_name = 'index.html'



def view_posts(request):
    context = {}
    posts = PostModel.objects.all()
    context['posts'] = posts
    return render(request, 'main.html', context)
