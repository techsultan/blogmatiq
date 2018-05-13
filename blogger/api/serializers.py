from rest_framework import serializers 
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost)

class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    pass 

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    pass 

class BlogCategorySeriaizer(serializers.HyperlinkedModelSerializer):
    pass 

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    pass 

