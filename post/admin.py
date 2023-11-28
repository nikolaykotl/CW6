from django.contrib import admin

from post.models import Post
from mail_service.models import Messages

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
from django.contrib import admin


