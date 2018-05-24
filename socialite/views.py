from django.shortcuts import render
 
# Create your views here.
def home(request):
    return render(request, "Socialite Home")


def facebook_share(request, page_url):
    data = {}
    return render(request, "socialite/facebook_share.html", data)

def twitter_share(request, page_url):
    data = {}
    return render(request, "socialite/twitter_share.html", data)

def linkedin_share(request, page_url):
    data = {}
    return render(request, "socialite/linkedin_share.html", data)
