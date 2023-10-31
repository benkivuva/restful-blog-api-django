from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_Create_Post(TestCase):
    """
    Test case for creating a blog post using Django's TestCase class.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data before running any test methods.

        This method creates a test category, a test user, and a test post to use in the tests.
        """
        test_category = Category.objects.create(name='events')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        """
        Test the content and properties of a created blog post.

        This test method retrieves the test blog post, category, and author, and then asserts that their properties are as expected.
        """
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "events")