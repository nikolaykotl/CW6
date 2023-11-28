from django.urls import path

from post.apps import PostConfig
from post.views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView

app_name = PostConfig.name



urlpatterns = [
    path('list', PostListView.as_view(), name='list'),
    path('create/',PostCreateView.as_view(), name='post_create'),
    path('view/<int:pk>', PostDetailView.as_view(), name='post_view'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')

]