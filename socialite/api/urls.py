from django.conf.urls import url 
#Import the format_suffix_patterns() for dynamic accept of requests for 
# JSON, XML, etc. API data response formats
from rest_framework.urlpatterns import format_suffix_patterns

from socialite.api import views

urlpatterns = [
    url(r'^$', views.socialite_api_root, name="socialite_api_root"),
    url(r'^users/$', views.UserListView.as_view(), name="user_list"),
    url(r'^socialites/$', views.SocialiteListView.as_view(), name="socialite_list"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name="user_detail"),
    url(r'^socialites/(?P<page>[-\w]+)/$', views.SocialiteDetailView.as_view(), name="socialite_detail")
]
urlpatterns = format_suffix_patterns(urlpatterns)