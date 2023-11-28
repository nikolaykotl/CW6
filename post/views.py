from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from config import settings
from post.models import Post
from post.servises import get_cache_post_list


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #form_class = PostForm
    fields = ('title', 'body', 'author', 'is_published', 'image')
    success_url = reverse_lazy('post:list')
    permission_required = 'mailing_service.add_post'
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        context_data['post'] = get_cache_post_list()
        return context_data

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count +=1
        self.object.save()
        return self.object



class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    success_url = reverse_lazy('post:list')
    permission_required = 'mailing_service.change_post'

class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')
    success_message = 'Статья удалена'
    permission_required = 'mailing_service.delete_post'