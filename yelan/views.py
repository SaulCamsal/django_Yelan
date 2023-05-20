from importlib import invalidate_caches
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index_view(request, path):
    """Home page view."""
    return render(request, 'index.html')
