from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    # now we need to get some posts... so a QuerySet from our db
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # the last param lets u give the template things to use
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # our view has an extra param to parse from the URL: the primary key
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        #save whatever we're posting w/ the form
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False) #the arg means we won't exactly save Post just yet
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else: #blank form
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})