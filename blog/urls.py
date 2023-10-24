from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    # Define a URL pattern for the root of the 'blog' app, which renders the 'index.html' template.
    path('', TemplateView.as_view(template_name="blog/index.html"), name='index'),
]