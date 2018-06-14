from blogger.models import (
	Blogger, Blog, BlogCategory, BlogPost, Comment
)
from blogger.api.serializers import (
	BloggerSerializer, BlogSerializer, BlogCategorySerializer,
	BlogPostSerializer, CommentSerializer
	)
from django.http import Http404 
from rest_framework import viewsets, generics
from rest_framework.reverse import reverse 
from rest_framework.response import Response 

#Import the filter classes and backends to use with the Blogger API 
from django_filters.rest_framework import DjangoFilterBackend
from  rest_framework import filters as drf_filters 

#Authentication and Permission classes for access to the API endpoints
from rest_framework.decorators import (api_view, authentication_classes)
from rest_framework.permissions import (
	IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
)

from rest_framework.authentication import (
	SessionAuthentication, BasicAuthentication, TokenAuthentication
)



def get_object(model_name, page):
    """
    A utility function to do a get on any Django model using its 'url' field
    """
    try:
        model_name.objects.get(page=page)
    except Object.DoesNotExist:
        raise Http404

@api_view(['GET'])
#@authentication_classes((SessionAuthentication,TokenAuthentication,))
def blogger_api_root(request, format=None):
    """
    URL endpoint to serve as the API Root (landing page) of the Blogger app's API.
    """
    return Response({
            'bloggers': reverse('blogger_api:blogger_list', request=request, format=format),
            'blogs': reverse('blogger_api:blog_list', request=request, format=format),
            'blogcategories': reverse('blogger_api:blogcategory_list', request=request, format=format),
            'blogposts': reverse('blogger_api:blogpost_list', request=request, format=format)
        })

class BloggerListView(generics.ListCreateAPIView):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
    #filter_fields = Blogger.filterable_fields
    #search_fields = Blogger.searchable_fields
    lookup_field = "page"

class BloggerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
    lookup_field = "page"

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    #filter_fields = Blog.filterable_fields
    #search_fields = Blog.searchable_fields
    lookup_field = "page"

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 
    lookup_field = "page"

class BlogCategoryListView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    filter_fields = BlogCategory.filterable_fields
    #search_fields = BlogCategory.searchable_fields
    lookup_field = "page"
    filter_backends = (DjangoFilterBackend,)

class BlogCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    filter_fields = BlogCategory.filterable_fields
    filter_backends = (DjangoFilterBackend,)
    lookup_field = "page"

class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = BlogPost.filterable_fields
    #search_fields = BlogPost.searchable_fields
    lookup_field  = "page"

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "page"
    filter_backends = (DjangoFilterBackend,)
    filter_fields = BlogPost.filterable_fields

class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    lookup_field = "page"