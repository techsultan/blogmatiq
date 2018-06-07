from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework import generics
from django.contrib.auth.models import User 
from socialite.models import Socialite

from socialite.api.serializers import (
    UserSerializer, SocialiteSerializer
)

@api_view(['GET'])
def blogmatiq_api_root(request, format=None):
    """
    The API root page for the Blogmatiq platform.
    It provides browsable links to the API roots/home pages of any component apps: blogger, socialite, etc.
    """
    return Response({
        'blogger': reverse('blogger_api:blogger_api_root', request=request, format=format),
        'socialite': reverse('socialite_api:socialite_api_root', request=request, format=format)
    })

@api_view(['GET'])
def socialite_api_root(request, format=None):
    """
    The root endpoint for the Socialite API.
    """
    return Response({
        'users': reverse('socialite_api:user_list', request=request, format=format),
        'socialites': reverse('socialite_api:socialite_list', request=request, format=format) 
    })

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    lookup_field = "pk"

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class SocialiteListView(generics.ListCreateAPIView):
    queryset = Socialite.objects.all()
    serializer_class = SocialiteSerializer
    lookup_field = "page"

class SocialiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Socialite.objects.all()
    serializer_class = SocialiteSerializer
    lookup_field = "page"