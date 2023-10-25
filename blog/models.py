from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    """
    Model representing categories for blog posts.

    Fields:
    - name (CharField): The name of the category (e.g., "Technology," "Lifestyle").
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Model representing individual blog posts.

    Fields:
    - category (ForeignKey): The category to which the post belongs.
    - title (CharField): The title of the blog post.
    - excerpt (TextField, optional): A short excerpt or summary of the post.
    - content (TextField): The main content of the post.
    - slug (SlugField): A slug that uniquely identifies the post based on its publication date.
    - published (DateTimeField): The date and time the post was published.
    - author (ForeignKey): The author of the post.
    - status (CharField): The publication status of the post (e.g., "draft" or "published").

    Managers:
    - objects: The default manager provided by Django.
    - postobjects: A custom manager for retrieving only published posts.

    Meta:
    - ordering: Default ordering for queries, showing the most recent posts first.

    Methods:
    - __str__: Returns the title of the post as its string representation.
    """

    class PostObjects(models.Manager):
        """
        Custom manager for filtering and retrieving only published blog posts.
        """
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
