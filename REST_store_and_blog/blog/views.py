from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.utils import timezone

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/listview.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detailview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ['title', 'text', 'author']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'text', 'author']

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:listview')
    template_name = 'blog/delete.html'
