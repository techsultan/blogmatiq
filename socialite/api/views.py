from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.reverse import reverse 

@api_view(['GET'])
def blogmatiq_api_root(request, format=None):
    """
    The API root page for the Blogmatiq platform.
    It provides browsable links to the API roots/home pages of any component apps: blogger, socialite, etc.
    """
    return Response({
        'blogger': reverse('blogger_api:blogger_api_root', request=request, format=format),
    })
