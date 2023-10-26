from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User

class PostTests(APITestCase):
    """
    Test case for the API views related to the 'Post' model.

    These tests ensure that we can view and create Post objects via the API.
    """

    def test_view_posts(self):
        """
        Test the ability to view all Post objects through the API.

        This test sends a GET request to the API endpoint that lists Post objects
        and checks if the response status code is HTTP 200 OK.
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        """
        Test the ability to create a new Post object via the API.

        This test creates a new Category and a User, then sends a POST request
        to create a new Post object. It checks if the response status code is HTTP 201 Created,
        if the response data has the expected length, and if the created object can be viewed.
        """
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 6)
        root = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
