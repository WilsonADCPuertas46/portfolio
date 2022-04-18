from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})


def post_detail(request, id):
    posts = get_object_or_404(Post, pk=id)
    return render(request, 'post_detail.html', {'posts': posts})