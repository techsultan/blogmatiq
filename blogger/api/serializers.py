from rest_framework import serializers 
from django.contrib.auth.models import User 
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost)
from blogmatiq.utils.models import get_model_field_names

class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    """
        BloggerSerializer is the API serializer for the blogger.Blogger model
        Default data format is JSON.
    """
    user = serializers.HyperlinkedRelatedField(
        queryset= User.objectd.all(),
        view_name = 'socialite_api:user_detail' ,
        lookup_field = "link"
    )
    blogs = serializers.HyperlinkedRelatedField(
        queryset =  Blog.objects.all(),
        view_name = "blog_api:blog_detail",
        lookup_field = "link"
    )
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Blogger 
        fields = get_model_field_names(Blogger, ['id']) + ('first_name', 'last_name', 'blog_url',)

    def get_blog_url(self, obj):
        """
        Returns the primary/first blog owned by this Blogger.
        """
        return obj.blogs.all()[0].link

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    """
    BlogSerializer is the API Serializer class for the blogger.Blog model
    """
    categories = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=BlogCategory.objects.all(),
        view_name='blog_api:blogcategory_detail',
        lookup_field="link"
        )
    owner = serializers.HyperlinkedRelatedField(
        queryset=Blogger.objects.all(),
        view_name="blog_api:blogger_detail",
        lookup_field = 'link')
    
    class Meta:
        model = Blog
        fields = get_model_field_names(Blog, ['id'])
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    pass 

class BlogCategorySeriaizer(serializers.HyperlinkedModelSerializer):
    pass 


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    pass 

