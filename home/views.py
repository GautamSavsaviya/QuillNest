from django.shortcuts import render
from blogs.models import Blog

# Create your views here.

# View for home page rendering
def index(request):
    blogs = Blog.objects.all()
    print(blogs)
    return render(request, 'home/index.html')


# View for about us page rendering
def about(request):
    return render(request, 'home/about_us.html')


# View for contact us page rendering
def contact(request):
    return render(request, 'home/contact_us.html')
