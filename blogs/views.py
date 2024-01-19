from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'base/base.html')