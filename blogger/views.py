from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    data = {

    }
    return render(request, "blogger/index.html", data)

def comment_on_post(request, post_link):
    data = {}
    return HttpResponse("Comment on %s " % (post_link))

def about(request):
    data = {}
    return render(request, "blogger/about.html", data)

def contact(request):
    data = {}
    return render(request, "blogger/contact.html", data)

def newsletter(request):
    data = {

    }
    return render(request, "blogger/newsletter.html", data)

def legal_terms(request):
    data = {}
    return render(request, "blogger/legal.html", data)