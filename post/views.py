from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from post.models import Post,Category


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context={
        "posts":posts,
        "categories":categories
    }
    return render(request, 'index.html', context=context)

def get_post_list(request):
    return render(request, "post_list.html")