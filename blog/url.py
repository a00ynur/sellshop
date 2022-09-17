from django.urls import path
from blog.views import BlogListView


urlpatterns = [
    path('blog/', BlogListView.as_view(), name="blog"),
]