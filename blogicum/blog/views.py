from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Category, Post


NUM_ON_MAIN = 5


def index(request) -> HttpResponse:
    template: str = 'blog/index.html'
    post_list: QuerySet = Post.objects.category_filter()[:NUM_ON_MAIN]
    context: dict = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id) -> HttpResponse:
    template: str = 'blog/detail.html'
    post: Post = get_object_or_404(Post.objects.category_filter(),
                                   pk=id)
    context: dict = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug) -> HttpResponse:
    category: Category = get_object_or_404(Category,
                                           is_published=True,
                                           slug=category_slug)
    post_list: QuerySet = category.posts_for_category.publish_filter()
    context: dict = {
        'category': category,
        'post_list': post_list,
    }
    template: str = 'blog/category.html'
    return render(request, template, context)
