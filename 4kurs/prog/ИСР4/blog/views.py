from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post
from .forms import PostForm

from django.db.models import Q

def posts_list(request):

    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(View):

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        return render(request, 'blog/post_detail.html', context={'post': post, 'detail': True})


class PostCreate(View):

    def get(self, request):
        form = PostForm
        return render(request, 'blog/post_create_form.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_create_form.html', context={'form': bound_form})


class PostUpdate(View):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        bound_form = PostForm(instance=post)
        return render(request, 'blog/post_update_form.html', context={'form': bound_form, 'post': post})

    def post(self, request, id):
        post = Post.objects.get(id=id)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_update_form.html', context={'form': bound_form, 'post': post})


class PostDelete(View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, 'blog/post_delete_form.html', context={'post': post})

    def post(self, request, id):
        post = Post.objects.get(id=id)
        post.delete()
        return redirect(reverse('posts_list_url'))