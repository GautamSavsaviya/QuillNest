from django.shortcuts import render
from blogs.models import Blog


# Create your views here.

# View for home page rendering
def index(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
    recent_blogs = blogs[:5]

    context = {
        'blogs': blogs,
        'recent_blogs': recent_blogs,
        'range': range(1, 5)
    }
    return render(request, 'home/index.html', context=context)


# View for about us page rendering
def about(request):
    return render(request, 'home/about_us.html')


# View for contact us page rendering
def contact(request):
    return render(request, 'home/contact_us.html')
