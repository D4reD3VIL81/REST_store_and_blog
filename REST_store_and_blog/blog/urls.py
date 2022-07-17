from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostDeleteView, PostUpdateView

app_name = 'blog'

urlpatterns = [
    path('listview/', PostListView.as_view(), name='listview'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detailview'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='update'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='delete'),
]
