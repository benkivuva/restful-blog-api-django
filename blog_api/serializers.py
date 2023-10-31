from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'Post' model.
    """

    class Meta:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
        model = Post
    """
    Metadata class for the 'PostSerializer'.
    """