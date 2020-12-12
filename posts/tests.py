from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='test_user', password='123456789')
        test_user.save()

        test_post = Post.objects.create(author=test_user, title='test title', body='test body')
        test_post.save()

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.author}', 'test_user')
        self.assertEqual(post.title, 'test title')
        self.assertEqual(post.body, 'test body')
