from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    all_post = Post.objects.all()
    output = ', '.join([ post.title for post in all_post ])
    return render(request,'blog/post_list.html',{})

def detail(request, post_id):
    return HttpResponse("You're looking at detail page for post id  %s." % post_id)

