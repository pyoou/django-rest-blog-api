from django.contrib import admin

from blog.models import Article, Category


class CategoryAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'name']


class ArticleAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'published', 'updated_at']
    list_filter = ['category', 'author', 'published', 'updated_at']

    list_per_page = 100
    search_fields = ['title', 'slug', 'author']


admin.site.register(Article, ArticleAdminConfig)
admin.site.register(Category, CategoryAdminConfig)
