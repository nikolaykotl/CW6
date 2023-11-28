from django.conf import settings
from django.core.cache import cache

from post.models import Post


def get_cache_post_list():
    if settings.CACHE_ENABLE:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Post.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Post.objects.all()
        return category_list