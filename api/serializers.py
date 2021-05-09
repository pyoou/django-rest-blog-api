from rest_framework import serializers
from blog.models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'image', 'slug', 'author', 'published', 'created_at', 'updated_at']
        # fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        # fields = '__all__'
