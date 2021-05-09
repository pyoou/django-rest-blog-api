from django.urls import path
from .views import ArticleListAPIView, ArticleDetailsAPIView, CategoryListAPIView, CategoryDetailsAPIView

urlpatterns = [
    path('article-list/', ArticleListAPIView.as_view(), name='ArticleList'),
    path('article-list/<slug:slug>/', ArticleDetailsAPIView.as_view(), name='ArticleDetails'),

    path('category-list/', CategoryListAPIView.as_view(), name='CategoryList'),
    path('category-list/<int:id>/', CategoryDetailsAPIView.as_view(), name='CategoryDetails'),
]
