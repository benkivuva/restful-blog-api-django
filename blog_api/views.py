from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """
    API View for listing and creating blog posts.

    This view allows listing all existing blog posts and creating new ones.

    Attributes:
        queryset (QuerySet): A queryset containing all blog posts.
        serializer_class (Serializer): The serializer class used to convert
            blog post data to and from JSON format.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    """
    API View for retrieving and deleting a specific blog post.

    This view allows retrieving the details of a specific blog post and
    deleting it.

    Attributes:
        queryset (QuerySet): A queryset containing all blog posts.
        serializer_class (Serializer): The serializer class used to convert
            blog post data to and from JSON format.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer