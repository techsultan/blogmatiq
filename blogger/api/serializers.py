from rest_framework import serializers 
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost)

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

