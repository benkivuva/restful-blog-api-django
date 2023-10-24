# Import necessary modules.
from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the project.
urlpatterns = [
    # Set up the admin interface URL pattern.
    path('admin/', admin.site.urls),

    # Include URL patterns from the 'blog' app with a 'blog' namespace.
    path('', include('blog.urls', namespace='blog')),

    # Include URL patterns from the 'blog_api' app with a 'blog_api' namespace.
    path('api/', include('blog_api.urls', namespace='blog_api')),
]
