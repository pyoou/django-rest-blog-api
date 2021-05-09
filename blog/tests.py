from django.test import TestCase
from .models import Article, Category
from accounts.models import NewUser


class TestCategoryModel(TestCase):

    def test_new_category(self):
        category = Category.objects.create(name='test_category')
        self.assertEqual(category.name, 'test_category')
        self.assertEqual(str(category), 'test_category')


class TestArticleModel(TestCase):

    def test_new_article(self):
        category = Category.objects.create(name='test_category')
        user = NewUser.objects.create_user('test@mail.com', 'username', 'firstname', 'lastname', 'password')
        article = Article.objects.create(
            title='test_title', content='test_content', category=category, slug='test_slug', author=user
        )
        self.assertEqual(article.title, 'test_title')
        self.assertEqual(article.content, 'test_content')
        self.assertEqual(article.category, category)
        self.assertEqual(article.slug, 'test_slug')
        self.assertEqual(article.author, user)
        self.assertEqual(str(article), "1")
