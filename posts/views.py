from allauth.account.views import PasswordChangeView
from django.urls import reverse

from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# Create your views here.


def index(request):
    return render(request, "posts/index.html")
    # return redirect('post-list')  # 메인을 글목록으로 설정한 것


def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():  # (1)
            new_post = post_form.save()
            return redirect('post-detail', post_id=new_post.id)
    else:
        post_form = PostForm()
    return render(request, 'posts/post_form.html', {'form': post_form})  # (2)


def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'posts/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context=context)


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # (1)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)  # (2)
        if post_form.is_valid():  # (3)
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else:  # GET-METHOD일 때
        post_form = PostForm(instance=post)  # (4)
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post': post})


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
