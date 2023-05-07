from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


# Create your tests here.
class TestPost(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='maks',
            password='Somepassword12345678'
        )
        cls.post = Post.objects.create(title='title', content='content', author=cls.user)

    def test_post(self):
        self.assertEqual(self.post.author.username, self.user.username)
        self.assertEqual(self.post.title, 'title')
        self.assertEqual(self.post.content, 'content')
        self.assertEqual(str(self.post), 'title')
