from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from pic_feed.models import Post

from .forms import PostForm

# Create your views here.
def landing(request):
    """View function for home page"""
    return render(request, "pic_feed/landing.html")

def feed(request):
    """View for the feed/home page of the app"""
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, "pic_feed/feed.html", context)

def create_post(request):
    if request.method != 'POST':
        # Not data submitted; create a black form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user

            new_post.save()
            form.save()
            return HttpResponseRedirect(Reversible('pic_feed:feed'))

    context = {'form': form}
    return render(request, 'pic_feed/create_post.html', context)