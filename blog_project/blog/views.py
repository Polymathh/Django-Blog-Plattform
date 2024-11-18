from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Post, Category, Comment
from .forms import PostForm, Comment


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.succes(request, f'Account created for {username}! You can now login. ')
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'blog/register.html', {'form': form})
    

def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)| Q(tags__name__icontains=query)
            ).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts, 'query':query})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail,' , pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_form.html',{'form':form})
    

def post_detail(request, pk):
    post = get=get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent=None)
    form = Comment()

    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author =request.user
            parent_id = request.POST.get(parent_id)
            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)
            comment.save()    
            return redirect('post_detail', pk=post.pk)
        

    return render(request, 'blog/post_detail.html',  {'post': post, 'comments': comments, 'form':form})

