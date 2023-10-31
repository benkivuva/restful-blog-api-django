from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission

class PostUserWritePermission(BasePermission):
    """
    Custom permission to restrict editing posts to the author only.
    """

    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the requested action on the post.

        Args:
            request: The HTTP request.
            view: The view handling the request.
            obj: The post instance.

        Returns:
            True if the user can perform the action, False otherwise.
        """

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    """
    API view for listing and creating blog posts.
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    """
    API view for retrieving, updating, and deleting a specific blog post.
    """

    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer