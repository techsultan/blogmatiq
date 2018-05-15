from rest_framework import serializers 
from django.utils.text import slugify 
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
    blogger = serializers.HyperlinkedRelatedField(
        queryset = Blogger.objects.all(),
        view_name = "blog_api:blogger_detail",
        lookup_field = "page"
    )
    page = serializers.SerializerMethodField()

    class Meta:
        model = User 
        fields = get_model_field_names(BlogPost, ['id'])+('blog_url','category_url')

    def get_page(self, obj):
        """
        Generates and returns a URL page for the User obj based on his/her first and last names.
        """
        return slugify(obj.first_name + obj.last_name)[:100]

class SocialiteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        queryset = User.objects.all(),
        view_name = 'socialite_api:user_detail',
        lookup_field = "page"
    )

    class Meta:
        model = Socialite 
        fields = get_model_field_names()