from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostDeleteView, PostUpdateView

app_name = 'blog'

urlpatterns = [
    path('list/', PostListView.as_view(), name='listview'),
    path('<int:pk>/', PostDetailView.as_view(), name='detailview'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete')
]
