from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(
            title = 'mytitle',
            body = 'just just'
        )
    def test_string_representation(self):
        post = Post(title='my entry')
        self.assertEqual(str(post), post.title)
    def test_post_list_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mytitle')
        self.assertTemplateUsed(response, 'blog/blog.html')
    def test_post_detail_view(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'mytitle')
        self.assertTemplateUsed(response, 'blog/post.html')