from django.urls import path

from .views import HomePageView, PostPaginationView, DetailPostView

app_name = 'post'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('posts/<slug:slug>/', PostPaginationView.as_view(), name='posts'),
    path('posts/<slug:slug_topic>/detail/<slug:slug_post>/', DetailPostView.as_view(), name='post_detail'),
]