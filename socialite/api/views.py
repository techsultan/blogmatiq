from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_viw(['GET'])
def blogmatiq_api_root(request, format=format):
    """
    The API root page for the Blogmatiq platform.
    It provides browsable links to the API roots/home paegs of any component apps: blogger, socialite, etc.
    """
    return Response({
        'blogger': reverse('blogger_api:blogger_api_root', request=request, format=format),
    })
