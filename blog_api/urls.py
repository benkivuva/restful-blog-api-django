from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    # URL pattern to display the details and allow editing of a specific post
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    
    # URL pattern to list and create new posts.
    path('', PostList.as_view(), name='listcreate'),
]