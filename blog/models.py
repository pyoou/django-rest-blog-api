from django.db import models
from accounts.models import NewUser
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):

    publish_choices = [
        ('public', 'public'),
        ('private', 'private'),
    ]

    title = models.CharField(verbose_name=_('article title'), max_length=255)
    content = models.TextField(verbose_name=_('content'))
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, to_field='id')
    image = models.ImageField(verbose_name=_('image'), null=True, blank=True, upload_to='images/')

    slug = models.SlugField(unique=True, max_length=60, allow_unicode=True)
    author = models.ForeignKey(NewUser, on_delete=models.RESTRICT, to_field='id')
    published = models.CharField(max_length=7, choices=publish_choices, default='private')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
