from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from blog.models import Blog, Tag
from django.db.models import Count


class BlogListView(ListView):
    model=Blog
    context_object_name='blogs'
    template_name='blog.html'
    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context["recent_posts"] = Blog.objects.order_by("-created_at")[:3]
        context["categories"] = Blog.objects.values('category__title').annotate(count = Count('category'))
        context['tags'] = Tag.objects.all()
        context['blogs'] = Blog.objects.all()
        return context