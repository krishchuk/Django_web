from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': "Новости"
    }


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data()

        item = Blog.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f"{item.title}"

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
