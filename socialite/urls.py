from django.conf.urls import url 
from socialite import views

urlpatterns = [
   url(r'^$', views.home, name="home"),
]
