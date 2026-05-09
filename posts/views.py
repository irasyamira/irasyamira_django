from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_posts_list = Post.objects.order_by("-pub_date")[:5]
    context = {"latest_posts_list": latest_posts_list}
    return render(request, "posts/index.html", context)
    # return HttpResponse("Hello, posts. First app setup complete!")