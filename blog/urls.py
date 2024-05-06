from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('news/', BlogListView.as_view(), name='blog_list'),
    path('news/<int:pk>', cache_page(300)(BlogDetailView.as_view()), name='blog_detail'),
]
