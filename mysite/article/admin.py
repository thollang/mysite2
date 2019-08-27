from django.contrib import admin
from .models import ArticleColumn


@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'created', 'user')
    list_filter = ('column',)
