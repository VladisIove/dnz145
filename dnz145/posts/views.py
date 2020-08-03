from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Topic, Post, File

class HomePageView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.filter(active=True).order_by('id').values('name', 'slug')
        return context


class PostPaginationView(ListView):
    template_name = 'pagination_posts.html'
    paginate_by = 3
    model = Post
    context_object_name = 'posts_list'

    def get_queryset(self):
        return self.model.objects.filter(active=True, topic__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_topic'] = self.kwargs['slug']
        topic =  Topic.objects.filter(active=True, slug=self.kwargs['slug']).values_list('name', flat=True)
        if topic:
            context['topic'] = topic[0]
        context['topics'] = Topic.objects.filter(active=True).order_by('id').values('name', 'slug')
        print(context)
        return context

class DetailPostView(DetailView):
    model = Post 
    queryset = Post.objects.filter(active=True)
    context_object_name = 'post'
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_topic'] = self.kwargs['slug_topic']
        context['topics'] = Topic.objects.filter(active=True).order_by('id').values('name', 'slug')
        return context

    def get_object(self, **kwargs):
        return self.queryset.filter(slug=self.kwargs['slug_post']).first()
