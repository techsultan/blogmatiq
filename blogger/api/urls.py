from django.conf.urls import url 
#Import the format_suffix_patterns() for dynamic accept of requests for 
# JSON, XML, etc. API data response formats
from rest_framework.urlpatterns import format_suffix_patterns

from blogger.api import views 

urlpatterns = format_suffix_patterns (
[  url(r'^$', views.blogger_api_root, name="blogger_api_root"),
   url(r'^bloggers/$', views.BloggerListView.as_view(), name="blogger_list"),
   url(r'^blogs/$', views.BlogListView.as_view(), name="blog_list"),
   url(r'^blogposts/$', views.BlogPostListView.as_view(), name="blogpost_list"),
   url(r'^comments/$', views.CommentListAPIView.as_view(), name="comment_list"), 
   url(r'^blogcategories/$', views.BlogCategoryListView.as_view(), name="blogcategory_list"),
   url(r'^bloggers/(?P<page>[-\w]+)/$', views.BloggerDetailView.as_view(), name="blogger_detail"),
   url(r'^blogs/(?P<page>[-\w]+)/$', views.BlogDetailView.as_view(), name="blog_detail"),
   url(r'^blogposts/(?P<page>[-\w]+)/$', views.BlogPostDetailView.as_view(), name="blogpost_detail"),
   url(r'^blogcategories/(?P<page>[-\w]+)/$', views.BlogCategoryDetailView.as_view(), name="blogcategory_detail"),
   
   ]
)
