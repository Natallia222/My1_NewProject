import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

user1 = User.objects.create_user('author1', 'author1@example.com', 'password1')
user2 = User.objects.create_user('author2', 'author2@example.com', 'password2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

cat1 = Category.objects.create(name='Спорт')
cat2 = Category.objects.create(name='Политика')
post1 = Post.objects.create(author=author1, post_type='AR', title='Тестовая статья', text='Текст статьи')
post2 = Post.objects.create(author=author2, post_type='NW', title='Тестовая новость', text='Текст новости')
Comment.objects.create(post=post1, user=user2, text='Комментарий к статье')
