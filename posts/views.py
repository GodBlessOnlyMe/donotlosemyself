from allauth.account.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView

from .forms import PostForm
from .models import Post


class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'  # redirect할 url name


def index(request):  # 로그인 창으로 보내려면 이 함수형 뷰를 사용할 것
    return render(request, 'posts/index.html')


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})  # (1)


class PostListView(ListView):
    model = Post
    ordering = ['-dt_created']  # 최신글부터 보이게
    paginate_by = 6  # pagination 단위


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post-list')


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
