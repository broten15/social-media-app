from django.shortcuts import render
from pic_feed.models import Post

# Create your views here.
def landing(request):
    """View function for home page"""
    return render(request, "pic_feed/landing.html")

def feed(request):
    """View for the feed/home page of the app"""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "pic_feed/feed.html", context)