from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from blog.models import Blog, Comment
from blog.forms import BlogForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def index(request):
    blog_list = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'blog_list':blog_list})


def about(request):
    return render(request, 'blog/about.html')


def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    #for comment adding functionality
    if request.method == "POST":
        comnt_form = CommentForm(request.POST)
        if comnt_form.is_valid:
            comnt_form = comnt_form.save(commit=False)
            comnt_form.blog = blog
            comnt_form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        comnt_form = CommentForm()

    return render(request, 'blog/detail.html', {'blog': blog, 'comnt_form':comnt_form})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid:
            blog = form.save(commit=False)
            blog.author = request.user
            if 'cover_pic' in request.FILES:
                blog.cover_pic = request.FILES['cover_pic']
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_create.html', {'form':form})

# @login_required
# def update_blog(request, blog_id):
#     blog = Blog.objects.get(pk=blog_id)
#     form = BlogForm(instance=blog)
#     fields = ('title', 'text')
#
#     if form.is_valid:
#         form.save()
#         return redirect('blog_detail', pk=blog_id)
#     return render(request, 'blog/blog_create.html', {'form':form})



@login_required
def draft_blogs(request):
    blog_list = Blog.objects.filter(published_date__isnull=True).order_by('-published_date')
    return render(request, 'blog/blog_drafts.html', {'blogs': blog_list})


@login_required
def blog_publish(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.publish()
    return redirect('index')


@login_required
def blog_delete(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect('index')


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment_blog_pk = comment.blog.pk
    comment.delete()
    return redirect('blog_detail', pk=comment_blog_pk)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('index')
            else:
                return render(request, 'blog/login.html', {'error_message':'Account has been temporarily disabled.'})
        else:
            return render(request, 'blog/login.html', {'error_message':'Invalid User Login.'})
    return render(request, 'blog/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
