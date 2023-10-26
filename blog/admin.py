from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Post model.

    This configuration defines how the Post model is displayed and managed
    in the Django admin interface.

    Attributes:
        list_display (tuple): A tuple of fields to display in the list view of posts.
        prepopulated_fields (dict): A dictionary specifying fields whose values are
            automatically generated based on the 'title' field.
    """
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.Category)
