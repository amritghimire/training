from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.

def index(request):
    all_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':all_post})

def detail(request, post_id):
    return HttpResponse("You're looking at detail page for post id  %s." % post_id)

