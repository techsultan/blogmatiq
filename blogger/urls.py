from django.conf.urls import url 
from blogger import views 

urlpatterns = [
    url(r'^$',views.home, name="home"),
]