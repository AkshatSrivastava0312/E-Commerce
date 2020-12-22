from django.shortcuts import render
from .models import Blogpost

# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts = Blogpost.objects.all()
    param = {'posts' : myposts}
    return render(request, 'blog/index.html', param)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    param = {'post' : post}
    return render(request, 'blog/blogpost.html', param)
