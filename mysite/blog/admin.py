from django.contrib import admin

# Register your models here.
from .models import BlogArticles


@admin.register(BlogArticles)
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-publish', 'author')
