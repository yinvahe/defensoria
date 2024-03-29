from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'defensora/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'defensora/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'defensora/post_edit.html', {'form': form})
    