from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the Django project
urlpatterns = [
    # Admin URLs: This directs to the Django admin interface
    path('admin/', admin.site.urls),

    # Include blog app URLs with a namespace called 'blog'
    path('', include('blog.urls', namespace='blog')),

    # Include blog API app URLs with a namespace called 'blog_api'
    path('api/', include('blog_api.urls', namespace='blog_api')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]