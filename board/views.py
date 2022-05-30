from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from django.utils import timezone

from  .models import Post
from django.http import HttpResponse

def index(request):
    postList = Post.objects.all()
    context = { 'postList': postList}
    return render(request, 'board/index.html', context)


def detail(request,postId):
    post = Post.objects.get(id = postId)
    context = {'post': post}
    return render(request, 'board/detail.html', context)

def answer_create(request,postId):
    post = get_object_or_404(Post, pk=postId)
    post.answer_set.create(content=request.POST.get('content'), date=timezone.now())
    return redirect('board:detail', postId=postId)
