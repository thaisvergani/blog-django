from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Comment, Post

def post_list(request): 
    context = {
        'posts':  []
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    context = {
        'post':  Post.objects.get(pk=pk),
        'comment_form': CommentForm()
    }
    return render(request, 'blog/post_detail.html', context)

def post_new(request):
    # from IPython import embed; embed()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', post.pk)
    else:     
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', post.pk)
    else:     
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
  
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect('post_detail', pk=post.pk)


def comment_upvote(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.upvote()

    return redirect('post_detail', pk=post_pk)

