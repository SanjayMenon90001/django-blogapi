from django.contrib import admin

# Register your models here.
from .models import Post, Comment
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')  # columns in list view
    list_filter = ('author', 'created')            # filters in the right sidebar
    search_fields = ('title', 'content')           # search box at the top

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created')
    list_filter = ('author', 'created', 'post')
    search_fields = ('content',)
