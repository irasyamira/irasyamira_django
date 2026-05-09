from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Post
# Create your views here.

def index(request):
    latest_posts_list = Post.objects.order_by("-pub_date")[:5]
    context = {"latest_posts_list": latest_posts_list}
    return render(request, "posts/index.html", context)

def detail(request, post_id):
    try:
        obj = Post.objects.get(pk=post_id)
        title = obj.title
        content = obj.content
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, "posts/detail.html", {"title": title,"content":content})