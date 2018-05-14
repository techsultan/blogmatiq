from rest_framework import serializers 
from django.contrib.auth.models import User 
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost)
from blogmatiq.utils.models import get_model_field_names
from socialite.models import Tag, Comment 
class BloggerSerializer(serializers.HyperlinkedModelSerializer):
    """
        BloggerSerializer is the API serializer for the blogger.Blogger model
        Default data format is JSON.
    """
    user = serializers.HyperlinkedRelatedField(
        queryset= User.objectd.all(),
        view_name = 'socialite_api:user_detail' ,
        lookup_field = "page"
    )
    blogs = serializers.HyperlinkedRelatedField(
        queryset =  Blog.objects.all(),
        view_name = "blog_api:blog_detail",
        lookup_field = "page"
    )
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Blogger 
        fields = get_model_field_names(Blogger, ['id']) + ('first_name', 'last_name', 'blog_url',)

    def get_blog_url(self, obj):
        """
        Returns the page link to the primary/first blog owned by this Blogger.
        """
        return obj.blogs.all()[0].page

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    """
    BlogSerializer is the API Serializer class for the blog.Blog model
    """
    categories = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=BlogCategory.objects.all(),
        view_name='blog_api:blogcategory_detail',
        lookup_field="page"
        )
    owner = serializers.HyperlinkedRelatedField(
        queryset=Blogger.objects.all(),
        view_name="blog_api:blogger_detail",
        lookup_field = 'page')
    
    class Meta:
        model = Blog
        fields = get_model_field_names(Blog, ['id'])

class BlogCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    BlogCategorySerializer is the serialized representation class for the blog.BlogCategory model
    """
    blog = serializers.HyperlinkedRelatedField(
        queryset = Blog.objects.all(),
        view_name ='blog_api:blog_detail',
        lookup_field ='page')
    blog_posts = serializers.HyperlinkedRelatedField(
        many=True, 
        queryset=BlogPost.objects.all(),
        view_name='blog_api:blogpost_detail',
        lookup_field="page") # OR JUST 'blog_api:blogposts' ??> TEST
    
    class Meta:
        model = BlogCategory 
        fields = get_model_field_names(BlogCategory, ['id'])

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    """
    BlogPostSerializer is the API's serialized representation of the blog.BlogPost model.
    """
    tags = serializers.HyperlinkedRelatedField(
        many=True, 
        queryset=Tag.objects.all(),
        view_name='socialite_api:tag_detail',
        lookup_field = "page"
        )
    category = serializers.HyperlinkedRelatedField(
        queryset = BlogCategory.objects.all(), 
        view_name='blog_api:blogcategory_detail',
        lookup_field="page")
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        queryset = Comment.objects.all(),
        view_name = "blog_api:comment_detail"
    )
    blog_url = serializers.SerializerMethodField()
    category_url = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost 
        fields = get_model_field_names(BlogPost, ['id'])+('blog_url','category_url')

    def get_blog_url(self, obj):
        return obj.category.blog.page

    def get_category_url(self, obj):
        return obj.category.page

