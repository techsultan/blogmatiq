from rest_framework import serializers 
from django.contrib.auth.models import User 
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost)
from blogmatiq.utils.models import get_model_field_names
from socialite.models import (Socialite,Tag, Comment)

class UserSerializer(serializers.ModelSerializer):
    socialite = serializers.HyperlinkedRelatedField(

    )
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        queryset = Comment.objects.all(),
        view_name = "blog_api:comment_detail",
        lookup_field = "page"
    )