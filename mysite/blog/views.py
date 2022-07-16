from django.shortcuts import render
from .models import Post

def post_list(request): 
    context = {
        'posts':  Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    context = {
        'post':  Post.objects.get(pk=pk)
    }
    return render(request, 'blog/post_detail.html', context)
