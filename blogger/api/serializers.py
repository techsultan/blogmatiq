from rest_framework import serializers 
from django.contrib.auth.models import User 
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost)
from blogmatiq.utils.models import get_model_field_names

class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    """
        BloggerSerializer is the API serializer for the blogger.Blogger model
    """
    user = serializers.HyperlinkedRelatedField(
        queryset= User.objectd.all(),
        view_name = 'socialite_api:user_detail' ,
        lookup_field = "link"
    )

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    pass 

class BlogCategorySeriaizer(serializers.HyperlinkedModelSerializer):
    pass 


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    pass 

